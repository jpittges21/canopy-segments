"""Create canopy_segments_submission.zip with the files to submit."""
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
INCLUDE = ["README.md", "src", "dags", "output", "docs", "notebooks"]

with zipfile.ZipFile(ROOT / "canopy_segments_submission.zip", "w", zipfile.ZIP_DEFLATED) as z:
    for item in INCLUDE:
        path = ROOT / item
        files = [path] if path.is_file() else [p for p in path.rglob("*") if p.is_file()]
        for f in files:
            if "__pycache__" in f.parts or ".ipynb_checkpoints" in f.parts:
                continue
            z.write(f, f.relative_to(ROOT))
print("Created", ROOT / "canopy_segments_submission.zip")
