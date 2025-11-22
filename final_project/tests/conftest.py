import sys
from pathlib import Path

# Ensure tests can import the package from `final_project/src` when running
# pytest from the repository root. This mirrors what an editable install or
# PYTHONPATH would provide but avoids requiring extra setup for contributors.
ROOT = Path(__file__).resolve().parents[1]  # final_project
SRC = ROOT / "src"

src_str = str(SRC)
if src_str not in sys.path:
    sys.path.insert(0, src_str)
