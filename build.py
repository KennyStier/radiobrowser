#!/usr/bin/env python3
"""Generate radio.m3u from stations.json. Run after editing stations.json."""
import json
from pathlib import Path

root = Path(__file__).resolve().parent
data = json.loads((root / "stations.json").read_text())
base = data["base_url"].rstrip("/") + "/"

lines = ["#EXTM3U"]
for s in data["stations"]:
    logo = base + s["logo"]
    lines.append(f'#EXTINF:-1 tvg-logo="{logo}" group-title="Radio",{s["name"]}')
    lines.append(s["stream"])

(root / "radio.m3u").write_text("\n".join(lines) + "\n")
print(f"wrote radio.m3u ({len(data['stations'])} stations)")
