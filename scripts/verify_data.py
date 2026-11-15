#!/usr/bin/env python3
"""Check the published CSV shapes and hashes without network access."""
import csv
import hashlib
import json
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "data"
manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
for name, spec in manifest["files"].items():
    path = ROOT / name
    assert hashlib.sha256(path.read_bytes()).hexdigest() == spec["sha256"], name
    with path.open(encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    assert len(rows) == spec["rows"], name
    if "solar-terms" in name:
        assert len(rows) == 384
        assert Counter(int(r["year"]) for r in rows) == {y: 24 for y in range(2020, 2036)}
        assert all(date.fromisoformat(r["date_local"]).year == int(r["year"]) for r in rows)
        assert len({(r["year"], r["solar_term_zh"]) for r in rows}) == 384
        assert Counter(r["value_kind"] for r in rows) == {"CWA published calendar": 48, "calculated estimate": 336}
    else:
        assert len(rows) == 480
        assert len({r["station_zh"] for r in rows}) == 5
        assert len({r["metric_code"] for r in rows}) == 8
        assert len({(r["station_zh"], r["metric_code"], r["month"]) for r in rows}) == 480
        assert all(r["normal_period"] == "1991-2020" for r in rows)
    print(f"{name}: {len(rows)} rows; SHA-256 matches")
