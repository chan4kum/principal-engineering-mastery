"""Evaluate versioned synthetic cases against independent observations."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Case:
    case_id: str
    expected: str
    tenant: str
    required_sources: frozenset[str]
    critical: bool = False


@dataclass(frozen=True)
class Response:
    answer: str
    tenant: str
    sources: frozenset[str]
    input_tokens: int
    output_tokens: int
    retrieval_tokens: int

    def cost_units(self, input_rate: int = 1, output_rate: int = 3) -> int:
        if not 0 <= self.retrieval_tokens <= self.input_tokens or self.output_tokens < 0:
            raise ValueError("invalid attribution")
        return self.input_tokens * input_rate + self.output_tokens * output_rate


def evaluate(cases, responses):
    """Return case-level evidence; missing and duplicate evidence prevent promotion."""
    case_ids = {case.case_id for case in cases}
    if not cases or len(case_ids) != len(cases) or set(responses) != case_ids:
        raise ValueError("incomplete or invalid golden-set evidence")
    return {
        case.case_id: {
            "answer": responses[case.case_id].answer == case.expected,
            "grounded": case.required_sources == responses[case.case_id].sources,
            "scope": (
                responses[case.case_id].tenant == case.tenant
                and all(
                    src.startswith(f"{case.tenant}:") for src in responses[case.case_id].sources
                )
            ),
            "critical": case.critical,
        }
        for case in cases
    }
