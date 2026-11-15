"""Run a FastAPI fixture and read its local OpenTelemetry instruments."""

import argparse
import asyncio
import json
from collections.abc import Awaitable, Callable

import httpx
from fastapi import FastAPI, HTTPException
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import InMemoryMetricReader
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from opentelemetry.sdk.trace.export.in_memory_span_exporter import InMemorySpanExporter
from opentelemetry.trace import StatusCode


class Dashboard:
    def __init__(self) -> None:
        self.reader = InMemoryMetricReader()
        self.meter_provider = MeterProvider(metric_readers=[self.reader])
        self.exporter = InMemorySpanExporter()
        self.tracer_provider = TracerProvider()
        self.tracer_provider.add_span_processor(SimpleSpanProcessor(self.exporter))
        meter = self.meter_provider.get_meter("pem.a08")
        self.requests = meter.create_counter("fixture.requests")
        self.duration = meter.create_histogram("fixture.duration", unit="ms")
        self.active = meter.create_up_down_counter("fixture.active")
        self.saturated = meter.create_counter("fixture.saturated")
        self.tracer = self.tracer_provider.get_tracer("pem.a08")

    def close(self) -> None:
        self.tracer_provider.shutdown()
        self.meter_provider.shutdown()

    def snapshot(self) -> dict[str, list[dict]]:
        batch = self.reader.get_metrics_data()
        points = []
        if batch is not None:
            for resource in batch.resource_metrics:
                for scope in resource.scope_metrics:
                    for metric in scope.metrics:
                        for point in metric.data.data_points:
                            values = (
                                {"count": point.count, "sum": point.sum}
                                if hasattr(point, "count")
                                else {"value": point.value}
                            )
                            points.append(
                                {
                                    "name": metric.name,
                                    "attributes": dict(point.attributes),
                                    **values,
                                }
                            )
        spans = [
            {
                "name": span.name,
                "trace_id": f"{span.context.trace_id:032x}",
                "status": span.status.status_code.name,
                "parent": f"{span.parent.span_id:016x}" if span.parent else None,
            }
            for span in self.exporter.get_finished_spans()
        ]
        return {"metrics": points, "spans": spans}


def create_app(
    dashboard: Dashboard, dependency: Callable[[], Awaitable[None]], slots: int = 1
) -> FastAPI:
    app = FastAPI()
    gate = asyncio.Semaphore(slots)

    @app.get("/work")
    async def work() -> dict[str, bool]:
        clock = asyncio.get_running_loop().time
        started = clock()
        status = 200
        with dashboard.tracer.start_as_current_span(
            "GET /work", record_exception=False
        ) as span:
            try:
                if gate.locked():
                    status = 503
                    dashboard.saturated.add(1)
                    raise HTTPException(status, "local fixture at capacity")
                async with gate:
                    dashboard.active.add(1)
                    try:
                        with dashboard.tracer.start_as_current_span(
                            "dependency", record_exception=False
                        ) as child:
                            try:
                                await dependency()
                            except OSError:
                                child.set_status(StatusCode.ERROR)
                                raise
                    finally:
                        dashboard.active.add(-1)
                return {"ok": True}
            except OSError as error:
                status = 503
                raise HTTPException(status, "local dependency unavailable") from error
            except asyncio.CancelledError:
                # Educational outcome distinct from an HTTP response code.
                status = 499
                raise
            finally:
                if status >= 500:
                    span.set_status(StatusCode.ERROR)
                attributes = {"route": "/work", "status": status}
                span.set_attribute("fixture.outcome", status)
                dashboard.requests.add(1, attributes)
                dashboard.duration.record((clock() - started) * 1000, attributes)

    return app


async def demo(broken: bool) -> dict:
    async def dependency() -> None:
        if broken:
            raise OSError("fixture dependency disconnected")
        await asyncio.sleep(0.01)

    dashboard = Dashboard()
    try:
        async with httpx.AsyncClient(
            transport=httpx.ASGITransport(app=create_app(dashboard, dependency)),
            base_url="http://fixture.test",
        ) as client:
            await client.get("/work", timeout=2)
        return dashboard.snapshot()
    finally:
        dashboard.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--break", dest="broken", action="store_true")
    args = parser.parse_args()
    print(json.dumps(asyncio.run(demo(args.broken)), indent=2))
