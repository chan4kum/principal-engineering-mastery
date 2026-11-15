FROM --platform=$BUILDPLATFORM python:3.12-slim AS source
WORKDIR /app
COPY server.py .
RUN python -m py_compile server.py

FROM python:3.12-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
COPY --from=source --chown=10001:10001 /app/server.py .
USER 10001:10001
EXPOSE 8080
CMD ["python", "/app/server.py"]
