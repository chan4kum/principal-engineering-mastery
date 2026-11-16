"""Verify both controls for every lesson and every local lab in the ten-module batch."""

from pathlib import Path
import subprocess
import sys

import pytest

ROOT = Path(__file__).resolve().parents[1]

CASES = {
    "01-architecture-A01-to-A20/A14-advanced-llmops-evals-safety/examples/A14.01.py": (
        "0.75",
        "1.0",
    ),
    "01-architecture-A01-to-A20/A14-advanced-llmops-evals-safety/examples/A14.02.py": (
        "0.75",
        "1.0",
    ),
    "01-architecture-A01-to-A20/A14-advanced-llmops-evals-safety/examples/A14.03.py": (
        "0.8",
        "0.7",
    ),
    "01-architecture-A01-to-A20/A14-advanced-llmops-evals-safety/examples/A14.04.py": ("4", "2"),
    "01-architecture-A01-to-A20/A14-advanced-llmops-evals-safety/examples/A14.05.py": (
        "560",
        "860",
    ),
    "01-architecture-A01-to-A20/A14-advanced-llmops-evals-safety/examples/A14.06.py": ("0", "1"),
    "01-architecture-A01-to-A20/A14-advanced-llmops-evals-safety/examples/A14.07.py": (
        "(0, 1)",
        "1",
    ),
    "01-architecture-A01-to-A20/A14-advanced-llmops-evals-safety/examples/A14.08.py": (
        "0.3333333333333333",
        "0.0",
    ),
    "01-architecture-A01-to-A20/A14-advanced-llmops-evals-safety/examples/A14.09.py": (
        "(0.6, 0.75)",
        "(0.7, 1)",
    ),
    "01-architecture-A01-to-A20/A14-advanced-llmops-evals-safety/examples/A14.10.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A14-advanced-llmops-evals-safety/examples/A14.11.py": (
        "('p1', 's1')",
        "('p1', 's2')",
    ),
    "01-architecture-A01-to-A20/A14-advanced-llmops-evals-safety/examples/A14.12.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A14-advanced-llmops-evals-safety/examples/A14.13.py": (
        "(4, 1024)",
        "(1, 512)",
    ),
    "01-architecture-A01-to-A20/A14-advanced-llmops-evals-safety/examples/A14.14.py": (
        "True",
        "False",
    ),
    "01-architecture-A01-to-A20/A14-advanced-llmops-evals-safety/examples/A14.15.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A14-advanced-llmops-evals-safety/examples/A14.16.py": (
        "(50, 70)",
        "(43.333333333333336, 43.333333333333336)",
    ),
    "01-architecture-A01-to-A20/A14-advanced-llmops-evals-safety/examples/A14.17.py": ("0.25", "1"),
    "01-architecture-A01-to-A20/A14-advanced-llmops-evals-safety/examples/A14.18.py": ("0.75", "1"),
    "01-architecture-A01-to-A20/A14-advanced-llmops-evals-safety/examples/A14.19.py": (
        "0.08",
        "0.2",
    ),
    "01-architecture-A01-to-A20/A14-advanced-llmops-evals-safety/examples/A14.20.py": ("2", "3"),
    "01-architecture-A01-to-A20/A14-advanced-llmops-evals-safety/examples/A14.21.py": ("1", "3"),
    "01-architecture-A01-to-A20/A14-advanced-llmops-evals-safety/examples/A14.22.py": (
        "-0.2",
        "0.0",
    ),
    "01-architecture-A01-to-A20/A14-advanced-llmops-evals-safety/examples/A14.23.py": (
        "(0, 0)",
        "(0, 2)",
    ),
    "01-architecture-A01-to-A20/A14-advanced-llmops-evals-safety/examples/A14.24.py": (
        "True",
        "False",
    ),
    "01-architecture-A01-to-A20/A14-advanced-llmops-evals-safety/examples/A14.25.py": (
        "'v1'",
        "'v2'",
    ),
    "01-architecture-A01-to-A20/A14-advanced-llmops-evals-safety/examples/A14.26.py": (
        "0.75",
        "1.5",
    ),
    "01-architecture-A01-to-A20/A14-advanced-llmops-evals-safety/examples/A14.27.py": (
        "10000",
        "6000",
    ),
    "01-architecture-A01-to-A20/A14-advanced-llmops-evals-safety/examples/A14.28.py": ("7", "30"),
    "01-architecture-A01-to-A20/A15-security-privacy-global-scale/examples/A15.01.py": (
        "(0.99, False)",
        "True",
    ),
    "01-architecture-A01-to-A20/A15-security-privacy-global-scale/examples/A15.02.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A15-security-privacy-global-scale/examples/A15.03.py": (
        "0.75",
        "1.0",
    ),
    "01-architecture-A01-to-A20/A15-security-privacy-global-scale/examples/A15.04.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A15-security-privacy-global-scale/examples/A15.05.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A15-security-privacy-global-scale/examples/A15.06.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A15-security-privacy-global-scale/examples/A15.07.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A15-security-privacy-global-scale/examples/A15.08.py": ("2", "5"),
    "01-architecture-A01-to-A20/A15-security-privacy-global-scale/examples/A15.09.py": ("2", "1"),
    "01-architecture-A01-to-A20/A15-security-privacy-global-scale/examples/A15.10.py": ("3", "9"),
    "01-architecture-A01-to-A20/A15-security-privacy-global-scale/examples/A15.11.py": ("2", "1"),
    "01-architecture-A01-to-A20/A15-security-privacy-global-scale/examples/A15.12.py": ("2", "0"),
    "01-architecture-A01-to-A20/A15-security-privacy-global-scale/examples/A15.13.py": ("1", "0"),
    "01-architecture-A01-to-A20/A15-security-privacy-global-scale/examples/A15.14.py": ("2", "1"),
    "01-architecture-A01-to-A20/A15-security-privacy-global-scale/examples/A15.15.py": ("3", "0"),
    "01-architecture-A01-to-A20/A15-security-privacy-global-scale/examples/A15.16.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A15-security-privacy-global-scale/examples/A15.17.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A15-security-privacy-global-scale/examples/A15.18.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A15-security-privacy-global-scale/examples/A15.19.py": (
        "0.6666666666666666",
        "1",
    ),
    "01-architecture-A01-to-A20/A15-security-privacy-global-scale/examples/A15.20.py": ("1", "0"),
    "01-architecture-A01-to-A20/A15-security-privacy-global-scale/examples/A15.21.py": (
        "(True, False)",
        "(False, True)",
    ),
    "01-architecture-A01-to-A20/A15-security-privacy-global-scale/examples/A15.22.py": ("0", "1"),
    "01-architecture-A01-to-A20/A15-security-privacy-global-scale/examples/A15.23.py": ("0", "1"),
    "01-architecture-A01-to-A20/A15-security-privacy-global-scale/examples/A15.24.py": ("6", "8"),
    "01-architecture-A01-to-A20/A15-security-privacy-global-scale/examples/A15.25.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A15-security-privacy-global-scale/examples/A15.26.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A15-security-privacy-global-scale/examples/A15.27.py": (
        "0.3333333333333333",
        "1.0",
    ),
    "01-architecture-A01-to-A20/A15-security-privacy-global-scale/examples/A15.28.py": (
        "(6, False)",
        "(6, True)",
    ),
    "01-architecture-A01-to-A20/A15-security-privacy-global-scale/examples/A15.29.py": ("1", "0"),
    "01-architecture-A01-to-A20/A16-system-design-and-interviews/examples/A16.01.py": ("1", "0"),
    "01-architecture-A01-to-A20/A16-system-design-and-interviews/examples/A16.02.py": (
        "0.75",
        "1.0",
    ),
    "01-architecture-A01-to-A20/A16-system-design-and-interviews/examples/A16.03.py": ("2", "4"),
    "01-architecture-A01-to-A20/A16-system-design-and-interviews/examples/A16.04.py": (
        "400",
        "100",
    ),
    "01-architecture-A01-to-A20/A16-system-design-and-interviews/examples/A16.05.py": ("50", "28"),
    "01-architecture-A01-to-A20/A16-system-design-and-interviews/examples/A16.06.py": ("1", "2"),
    "01-architecture-A01-to-A20/A16-system-design-and-interviews/examples/A16.07.py": ("10", "100"),
    "01-architecture-A01-to-A20/A16-system-design-and-interviews/examples/A16.08.py": ("1", "2"),
    "01-architecture-A01-to-A20/A16-system-design-and-interviews/examples/A16.09.py": (
        "0.4",
        "2.5",
    ),
    "01-architecture-A01-to-A20/A16-system-design-and-interviews/examples/A16.10.py": (
        "150",
        "400",
    ),
    "01-architecture-A01-to-A20/A16-system-design-and-interviews/examples/A16.11.py": ("64", "16"),
    "01-architecture-A01-to-A20/A16-system-design-and-interviews/examples/A16.12.py": ("10", "40"),
    "01-architecture-A01-to-A20/A16-system-design-and-interviews/examples/A16.13.py": ("1", "2"),
    "01-architecture-A01-to-A20/A16-system-design-and-interviews/examples/A16.14.py": ("2", "3"),
    "01-architecture-A01-to-A20/A16-system-design-and-interviews/examples/A16.15.py": ("2", "3"),
    "01-architecture-A01-to-A20/A16-system-design-and-interviews/examples/A16.16.py": ("600", "3"),
    "01-architecture-A01-to-A20/A16-system-design-and-interviews/examples/A16.17.py": ("1", "2"),
    "01-architecture-A01-to-A20/A16-system-design-and-interviews/examples/A16.18.py": ("0.5", "1"),
    "01-architecture-A01-to-A20/A16-system-design-and-interviews/examples/A16.19.py": ("2", "1"),
    "01-architecture-A01-to-A20/A16-system-design-and-interviews/examples/A16.20.py": ("3", "4"),
    "01-architecture-A01-to-A20/A16-system-design-and-interviews/examples/A16.21.py": ("48", "24"),
    "01-architecture-A01-to-A20/A16-system-design-and-interviews/examples/A16.22.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A16-system-design-and-interviews/examples/A16.23.py": (
        "120",
        "960",
    ),
    "01-architecture-A01-to-A20/A16-system-design-and-interviews/examples/A16.24.py": ("20", "5"),
    "01-architecture-A01-to-A20/A16-system-design-and-interviews/examples/A16.25.py": ("6", "2"),
    "01-architecture-A01-to-A20/A16-system-design-and-interviews/examples/A16.26.py": ("4", "7"),
    "01-architecture-A01-to-A20/A16-system-design-and-interviews/examples/A16.27.py": ("1", "0"),
    "01-architecture-A01-to-A20/A16-system-design-and-interviews/examples/A16.28.py": ("2", "0"),
    "01-architecture-A01-to-A20/A16-system-design-and-interviews/examples/A16.29.py": ("8", "6"),
    "01-architecture-A01-to-A20/A16-system-design-and-interviews/examples/A16.30.py": ("1", "2"),
    "01-architecture-A01-to-A20/A16-system-design-and-interviews/examples/A16.31.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A16-system-design-and-interviews/examples/A16.32.py": ("1", "2"),
    "01-architecture-A01-to-A20/A16-system-design-and-interviews/examples/A16.33.py": (
        "16000000",
        "1000000",
    ),
    "01-architecture-A01-to-A20/A16-system-design-and-interviews/examples/A16.34.py": ("1", "0"),
    "01-architecture-A01-to-A20/A17-regulated-ai-compliance-governance/examples/A17.01.py": (
        "2",
        "1",
    ),
    "01-architecture-A01-to-A20/A17-regulated-ai-compliance-governance/examples/A17.02.py": (
        "0.6",
        "1.0",
    ),
    "01-architecture-A01-to-A20/A17-regulated-ai-compliance-governance/examples/A17.03.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A17-regulated-ai-compliance-governance/examples/A17.04.py": (
        "1",
        "0",
    ),
    "01-architecture-A01-to-A20/A17-regulated-ai-compliance-governance/examples/A17.05.py": (
        "0",
        "1",
    ),
    "01-architecture-A01-to-A20/A17-regulated-ai-compliance-governance/examples/A17.06.py": (
        "1",
        "0",
    ),
    "01-architecture-A01-to-A20/A17-regulated-ai-compliance-governance/examples/A17.07.py": (
        "3",
        "1",
    ),
    "01-architecture-A01-to-A20/A17-regulated-ai-compliance-governance/examples/A17.08.py": (
        "0.75",
        "1",
    ),
    "01-architecture-A01-to-A20/A17-regulated-ai-compliance-governance/examples/A17.09.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A17-regulated-ai-compliance-governance/examples/A17.10.py": (
        "1",
        "0",
    ),
    "01-architecture-A01-to-A20/A17-regulated-ai-compliance-governance/examples/A17.11.py": (
        "1",
        "0",
    ),
    "01-architecture-A01-to-A20/A17-regulated-ai-compliance-governance/examples/A17.12.py": (
        "0.6666666666666666",
        "1",
    ),
    "01-architecture-A01-to-A20/A17-regulated-ai-compliance-governance/examples/A17.13.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A17-regulated-ai-compliance-governance/examples/A17.14.py": (
        "1",
        "0",
    ),
    "01-architecture-A01-to-A20/A17-regulated-ai-compliance-governance/examples/A17.15.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A17-regulated-ai-compliance-governance/examples/A17.16.py": (
        "2",
        "3",
    ),
    "01-architecture-A01-to-A20/A17-regulated-ai-compliance-governance/examples/A17.17.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A17-regulated-ai-compliance-governance/examples/A17.18.py": (
        "True",
        "False",
    ),
    "01-architecture-A01-to-A20/A17-regulated-ai-compliance-governance/examples/A17.19.py": (
        "0.6666666666666666",
        "1",
    ),
    "01-architecture-A01-to-A20/A17-regulated-ai-compliance-governance/examples/A17.20.py": (
        "1",
        "0",
    ),
    "01-architecture-A01-to-A20/A17-regulated-ai-compliance-governance/examples/A17.21.py": (
        "True",
        "False",
    ),
    "01-architecture-A01-to-A20/A17-regulated-ai-compliance-governance/examples/A17.22.py": (
        "1",
        "0",
    ),
    "01-architecture-A01-to-A20/A17-regulated-ai-compliance-governance/examples/A17.23.py": (
        "1",
        "0",
    ),
    "01-architecture-A01-to-A20/A17-regulated-ai-compliance-governance/examples/A17.24.py": (
        "1",
        "0",
    ),
    "01-architecture-A01-to-A20/A17-regulated-ai-compliance-governance/examples/A17.25.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A17-regulated-ai-compliance-governance/examples/A17.26.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A18-microsoft-foundry-enterprise-ai/examples/A18.01.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A18-microsoft-foundry-enterprise-ai/examples/A18.02.py": ("0", "1"),
    "01-architecture-A01-to-A20/A18-microsoft-foundry-enterprise-ai/examples/A18.03.py": (
        "0.5",
        "0.9",
    ),
    "01-architecture-A01-to-A20/A18-microsoft-foundry-enterprise-ai/examples/A18.04.py": ("1", "0"),
    "01-architecture-A01-to-A20/A18-microsoft-foundry-enterprise-ai/examples/A18.05.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A18-microsoft-foundry-enterprise-ai/examples/A18.06.py": (
        "0.06",
        "60.0",
    ),
    "01-architecture-A01-to-A20/A18-microsoft-foundry-enterprise-ai/examples/A18.07.py": ("1", "2"),
    "01-architecture-A01-to-A20/A18-microsoft-foundry-enterprise-ai/examples/A18.08.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A18-microsoft-foundry-enterprise-ai/examples/A18.09.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A18-microsoft-foundry-enterprise-ai/examples/A18.10.py": ("1", "2"),
    "01-architecture-A01-to-A20/A18-microsoft-foundry-enterprise-ai/examples/A18.11.py": ("1", "3"),
    "01-architecture-A01-to-A20/A18-microsoft-foundry-enterprise-ai/examples/A18.12.py": ("1", "2"),
    "01-architecture-A01-to-A20/A18-microsoft-foundry-enterprise-ai/examples/A18.13.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A18-microsoft-foundry-enterprise-ai/examples/A18.14.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A18-microsoft-foundry-enterprise-ai/examples/A18.15.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A18-microsoft-foundry-enterprise-ai/examples/A18.16.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A18-microsoft-foundry-enterprise-ai/examples/A18.17.py": (
        "0.6666666666666666",
        "1",
    ),
    "01-architecture-A01-to-A20/A18-microsoft-foundry-enterprise-ai/examples/A18.18.py": (
        "10",
        "5",
    ),
    "01-architecture-A01-to-A20/A18-microsoft-foundry-enterprise-ai/examples/A18.19.py": ("2", "8"),
    "01-architecture-A01-to-A20/A18-microsoft-foundry-enterprise-ai/examples/A18.20.py": (
        "(2, 2, 0)",
        "(2, 0, 0)",
    ),
    "01-architecture-A01-to-A20/A18-microsoft-foundry-enterprise-ai/examples/A18.21.py": ("1", "0"),
    "01-architecture-A01-to-A20/A18-microsoft-foundry-enterprise-ai/examples/A18.22.py": (
        "(10, 30)",
        "(20, 20)",
    ),
    "01-architecture-A01-to-A20/A18-microsoft-foundry-enterprise-ai/examples/A18.23.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A18-microsoft-foundry-enterprise-ai/examples/A18.24.py": ("1", "0"),
    "01-architecture-A01-to-A20/A18-microsoft-foundry-enterprise-ai/examples/A18.25.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A18-microsoft-foundry-enterprise-ai/examples/A18.26.py": ("0", "1"),
    "01-architecture-A01-to-A20/A19-voice-multimodal-edge-embedded-ai/examples/A19.01.py": (
        "8000",
        "16000",
    ),
    "01-architecture-A01-to-A20/A19-voice-multimodal-edge-embedded-ai/examples/A19.02.py": (
        "(400, 160)",
        "(25, 10)",
    ),
    "01-architecture-A01-to-A20/A19-voice-multimodal-edge-embedded-ai/examples/A19.03.py": (
        "32000",
        "64000",
    ),
    "01-architecture-A01-to-A20/A19-voice-multimodal-edge-embedded-ai/examples/A19.04.py": (
        "0.3",
        "0.1",
    ),
    "01-architecture-A01-to-A20/A19-voice-multimodal-edge-embedded-ai/examples/A19.05.py": (
        "340",
        "180",
    ),
    "01-architecture-A01-to-A20/A19-voice-multimodal-edge-embedded-ai/examples/A19.06.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A19-voice-multimodal-edge-embedded-ai/examples/A19.07.py": (
        "15",
        "8",
    ),
    "01-architecture-A01-to-A20/A19-voice-multimodal-edge-embedded-ai/examples/A19.08.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A19-voice-multimodal-edge-embedded-ai/examples/A19.09.py": (
        "1",
        "3",
    ),
    "01-architecture-A01-to-A20/A19-voice-multimodal-edge-embedded-ai/examples/A19.10.py": (
        "0.1",
        "2",
    ),
    "01-architecture-A01-to-A20/A19-voice-multimodal-edge-embedded-ai/examples/A19.11.py": (
        "[2]",
        "[1, 2, 1]",
    ),
    "01-architecture-A01-to-A20/A19-voice-multimodal-edge-embedded-ai/examples/A19.12.py": (
        "1",
        "3",
    ),
    "01-architecture-A01-to-A20/A19-voice-multimodal-edge-embedded-ai/examples/A19.13.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A19-voice-multimodal-edge-embedded-ai/examples/A19.14.py": (
        "1",
        "2",
    ),
    "01-architecture-A01-to-A20/A19-voice-multimodal-edge-embedded-ai/examples/A19.15.py": (
        "(4000, 1000)",
        "(4000, 4000)",
    ),
    "01-architecture-A01-to-A20/A19-voice-multimodal-edge-embedded-ai/examples/A19.16.py": (
        "(0.6, 100)",
        "(0.6, 40)",
    ),
    "01-architecture-A01-to-A20/A19-voice-multimodal-edge-embedded-ai/examples/A19.17.py": (
        "(0.7, 0.3)",
        "(1, 0)",
    ),
    "01-architecture-A01-to-A20/A19-voice-multimodal-edge-embedded-ai/examples/A19.18.py": (
        "1",
        "0",
    ),
    "01-architecture-A01-to-A20/A19-voice-multimodal-edge-embedded-ai/examples/A19.19.py": (
        "1",
        "0",
    ),
    "01-architecture-A01-to-A20/A19-voice-multimodal-edge-embedded-ai/examples/A19.20.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A19-voice-multimodal-edge-embedded-ai/examples/A19.21.py": (
        "60",
        "120",
    ),
    "01-architecture-A01-to-A20/A19-voice-multimodal-edge-embedded-ai/examples/A19.22.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A19-voice-multimodal-edge-embedded-ai/examples/A19.23.py": (
        "20",
        "400",
    ),
    "01-architecture-A01-to-A20/A19-voice-multimodal-edge-embedded-ai/examples/A19.24.py": (
        "1",
        "0",
    ),
    "01-architecture-A01-to-A20/A19-voice-multimodal-edge-embedded-ai/examples/A19.25.py": (
        "2",
        "0",
    ),
    "01-architecture-A01-to-A20/A19-voice-multimodal-edge-embedded-ai/examples/A19.26.py": (
        "'v1'",
        "'v2'",
    ),
    "01-architecture-A01-to-A20/A19-voice-multimodal-edge-embedded-ai/examples/A19.27.py": (
        "1",
        "2",
    ),
    "01-architecture-A01-to-A20/A19-voice-multimodal-edge-embedded-ai/examples/A19.28.py": (
        "0.1",
        "0.04",
    ),
    "01-architecture-A01-to-A20/A19-voice-multimodal-edge-embedded-ai/examples/A19.29.py": (
        "(90, 200, 410)",
        "(410, 410, 410)",
    ),
    "01-architecture-A01-to-A20/A19-voice-multimodal-edge-embedded-ai/examples/A19.30.py": (
        "1",
        "0",
    ),
    "01-architecture-A01-to-A20/A19-voice-multimodal-edge-embedded-ai/examples/A19.31.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A20-forward-deployed-product-leadership/examples/A20.01.py": (
        "18",
        "25",
    ),
    "01-architecture-A01-to-A20/A20-forward-deployed-product-leadership/examples/A20.02.py": (
        "3",
        "2",
    ),
    "01-architecture-A01-to-A20/A20-forward-deployed-product-leadership/examples/A20.03.py": (
        "0.25",
        "5",
    ),
    "01-architecture-A01-to-A20/A20-forward-deployed-product-leadership/examples/A20.04.py": (
        "4",
        "0",
    ),
    "01-architecture-A01-to-A20/A20-forward-deployed-product-leadership/examples/A20.05.py": (
        "True",
        "False",
    ),
    "01-architecture-A01-to-A20/A20-forward-deployed-product-leadership/examples/A20.06.py": (
        "1",
        "0",
    ),
    "01-architecture-A01-to-A20/A20-forward-deployed-product-leadership/examples/A20.07.py": (
        "1",
        "0",
    ),
    "01-architecture-A01-to-A20/A20-forward-deployed-product-leadership/examples/A20.08.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A20-forward-deployed-product-leadership/examples/A20.09.py": (
        "0.6",
        "1",
    ),
    "01-architecture-A01-to-A20/A20-forward-deployed-product-leadership/examples/A20.10.py": (
        "0.5",
        "1",
    ),
    "01-architecture-A01-to-A20/A20-forward-deployed-product-leadership/examples/A20.11.py": (
        "1",
        "0",
    ),
    "01-architecture-A01-to-A20/A20-forward-deployed-product-leadership/examples/A20.12.py": (
        "1",
        "2",
    ),
    "01-architecture-A01-to-A20/A20-forward-deployed-product-leadership/examples/A20.13.py": (
        "1",
        "2",
    ),
    "01-architecture-A01-to-A20/A20-forward-deployed-product-leadership/examples/A20.14.py": (
        "1",
        "0",
    ),
    "01-architecture-A01-to-A20/A20-forward-deployed-product-leadership/examples/A20.15.py": (
        "80",
        "40",
    ),
    "01-architecture-A01-to-A20/A20-forward-deployed-product-leadership/examples/A20.16.py": (
        "10",
        "14",
    ),
    "01-architecture-A01-to-A20/A20-forward-deployed-product-leadership/examples/A20.17.py": (
        "1",
        "3",
    ),
    "01-architecture-A01-to-A20/A20-forward-deployed-product-leadership/examples/A20.18.py": (
        "1",
        "0",
    ),
    "01-architecture-A01-to-A20/A20-forward-deployed-product-leadership/examples/A20.19.py": (
        "1",
        "3",
    ),
    "01-architecture-A01-to-A20/A20-forward-deployed-product-leadership/examples/A20.20.py": (
        "0.75",
        "1",
    ),
    "01-architecture-A01-to-A20/A20-forward-deployed-product-leadership/examples/A20.21.py": (
        "1",
        "0",
    ),
    "01-architecture-A01-to-A20/A20-forward-deployed-product-leadership/examples/A20.22.py": (
        "1",
        "2",
    ),
    "01-architecture-A01-to-A20/A20-forward-deployed-product-leadership/examples/A20.23.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A20-forward-deployed-product-leadership/examples/A20.24.py": (
        "0.6666666666666666",
        "1",
    ),
    "01-architecture-A01-to-A20/A20-forward-deployed-product-leadership/examples/A20.25.py": (
        "False",
        "True",
    ),
    "01-architecture-A01-to-A20/A20-forward-deployed-product-leadership/examples/A20.26.py": (
        "0.5",
        "1.5",
    ),
    "01-architecture-A01-to-A20/A20-forward-deployed-product-leadership/examples/A20.27.py": (
        "2.0",
        "0.002",
    ),
    "01-architecture-A01-to-A20/A20-forward-deployed-product-leadership/examples/A20.28.py": (
        "1",
        "2",
    ),
    "01-architecture-A01-to-A20/A20-forward-deployed-product-leadership/examples/A20.29.py": (
        "1",
        "3",
    ),
    "01-architecture-A01-to-A20/A20-forward-deployed-product-leadership/examples/A20.30.py": (
        "1",
        "0",
    ),
    "02-mathematics-M01-to-M13/M01-sets-and-mathematical-language/examples/M01.01.py": (
        "(1.5, (-1+0j))",
        "(1, 1)",
    ),
    "02-mathematics-M01-to-M13/M01-sets-and-mathematical-language/examples/M01.02.py": ("-9", "9"),
    "02-mathematics-M01-to-M13/M01-sets-and-mathematical-language/examples/M01.03.py": (
        "(True, True)",
        "(False, False)",
    ),
    "02-mathematics-M01-to-M13/M01-sets-and-mathematical-language/examples/M01.04.py": (
        "[-2, 0, 2]",
        "[2]",
    ),
    "02-mathematics-M01-to-M13/M01-sets-and-mathematical-language/examples/M01.05.py": (
        "(3, 1, 1)",
        "(2, 2, 2)",
    ),
    "02-mathematics-M01-to-M13/M01-sets-and-mathematical-language/examples/M01.06.py": ("6", "2"),
    "02-mathematics-M01-to-M13/M01-sets-and-mathematical-language/examples/M01.07.py": (
        "[-0.5, 0.5]",
        "[-0.5, 0, 0.5]",
    ),
    "02-mathematics-M01-to-M13/M01-sets-and-mathematical-language/examples/M01.08.py": ("2", "1"),
    "02-mathematics-M01-to-M13/M02-logic-and-proof/examples/M02.01.py": ("True", "False"),
    "02-mathematics-M01-to-M13/M02-logic-and-proof/examples/M02.02.py": ("[2, 4]", "[2]"),
    "02-mathematics-M01-to-M13/M02-logic-and-proof/examples/M02.03.py": (
        "[0, 1, 1, 1]",
        "[0, 1, 1, 0]",
    ),
    "02-mathematics-M01-to-M13/M02-logic-and-proof/examples/M02.04.py": ("(True, True)", "False"),
    "02-mathematics-M01-to-M13/M02-logic-and-proof/examples/M02.05.py": ("True", "False"),
    "02-mathematics-M01-to-M13/M02-logic-and-proof/examples/M02.06.py": ("True", "False"),
    "02-mathematics-M01-to-M13/M02-logic-and-proof/examples/M02.07.py": ("0", "1"),
    "02-mathematics-M01-to-M13/M02-logic-and-proof/examples/M02.08.py": ("10", "6"),
    "02-mathematics-M01-to-M13/M03-linear-systems/examples/M03.01.py": ("[4, 6]", "[2, 6]"),
    "02-mathematics-M01-to-M13/M03-linear-systems/examples/M03.02.py": ("[0, 0]", "[0, 2]"),
    "02-mathematics-M01-to-M13/M03-linear-systems/examples/M03.03.py": ("1", "0"),
    "02-mathematics-M01-to-M13/M03-linear-systems/examples/M03.04.py": ("1", "2"),
    "02-mathematics-M01-to-M13/M03-linear-systems/examples/M03.05.py": ("10", "12"),
    "02-mathematics-M01-to-M13/M03-linear-systems/examples/M03.06.py": ("1", "0"),
    "02-mathematics-M01-to-M13/M03-linear-systems/examples/M03.07.py": ("1000.0", "10.0"),
}


@pytest.mark.parametrize("relative, expected", list(CASES.items()))
@pytest.mark.parametrize("broken", [False, True], ids=["normal", "changed"])
def test_lesson_controls(relative, expected, broken):
    path = ROOT / relative
    command = [sys.executable, str(path)] + (["--break"] if broken else [])
    assert subprocess.check_output(command, text=True, timeout=15).strip() == expected[int(broken)]


ARCH = ROOT / "01-architecture-A01-to-A20"
MATH = ROOT / "02-mathematics-M01-to-M13"
MODULES = [next(ARCH.glob(f"A{number:02d}-*")) for number in range(14, 21)]
MODULES += [next(MATH.glob(f"M{number:02d}-*")) for number in range(1, 4)]


@pytest.mark.parametrize("module", MODULES, ids=lambda path: path.name[:3])
@pytest.mark.parametrize("lab", range(1, 5))
@pytest.mark.parametrize("broken", [False, True], ids=["normal", "changed"])
def test_project_lab_controls(module, lab, broken):
    if module.parent == MATH:
        pytest.importorskip("numpy")
    path = module / "labs" / "verify.py"
    command = [sys.executable, str(path), f"L{lab}"] + (["--break"] if broken else [])
    label = "failure control" if broken else "normal control"
    assert subprocess.check_output(command, text=True, timeout=15).startswith(f"L{lab} {label}:")


NOTEBOOKS = sorted(MATH.glob("M*/projects/*/verify.ipynb"))


@pytest.mark.parametrize(
    "notebook", NOTEBOOKS, ids=lambda path: f"{path.parents[2].name[:3]}-{path.parent.name}"
)
@pytest.mark.parametrize("from_root", [True, False], ids=["repo", "project"])
def test_math_notebook_cells_execute(notebook, from_root):
    import json

    pytest.importorskip("numpy")
    cells = json.loads(notebook.read_text())["cells"]
    code = "\n".join("".join(cell["source"]) for cell in cells if cell["cell_type"] == "code")
    subprocess.run(
        [sys.executable, "-c", code],
        cwd=ROOT if from_root else notebook.parent,
        check=True,
        timeout=15,
    )
