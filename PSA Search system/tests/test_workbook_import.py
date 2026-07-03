import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.export_workbook import export_workbook


def test_export_workbook_creates_json_payload():
    payload = export_workbook()
    assert payload["file"] == "032026_Sorted PSOC PSIC.xlsx"
    assert len(payload["sheets"]) >= 1
    assert payload["sheets"][0]["name"]
    assert payload["sheets"][0]["rows"] is not None

    output_path = Path("data/psa-data.json")
    assert output_path.exists()
    data = json.loads(output_path.read_text(encoding="utf-8"))
    assert data["file"] == payload["file"]
