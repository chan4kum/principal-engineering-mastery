"""Run local oversight and provenance scenarios."""

from dataclasses import asdict

from guided import Request, triage
from independent import Approval, Audit, digest, verify


def observe(lab, broken):
    request = Request("fixture-1", "administrative-draft", "source-2", "operator")
    sources = set() if broken and lab == 1 else {"source-2"}
    if lab == 1:
        return triage(request, {"administrative-draft"}, sources)
    audit = Audit(sources, {"reviewer"})
    approval = Approval("reviewer", "old" if broken and lab == 2 else digest(asdict(request)), 5)
    passed = audit.execute(request, approval, 7 if broken and lab == 3 else 1)
    if lab in {2, 3}:
        return (passed, len(audit.effects))
    audit.execute(request, approval, 2)
    anchor = audit.events[-1]["hash"]
    if broken:
        audit.events[0]["result"] = "changed"
    return (verify(audit.events, anchor), len(audit.effects))


EXPECTED = (
    ("needs review", "needs evidence"),
    ((True, 1), (False, 0)),
    ((True, 1), (False, 0)),
    ((True, 1), (False, 1)),
)
