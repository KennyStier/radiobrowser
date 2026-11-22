#!/usr/bin/env python3
"""Export stations.json in RadioBrowser's radio-database format.

Writes two files to radiobrowser-export/:
  update-existing.json  Stations already on RadioBrowser (have a `radiobrowser` UUID).
                        Submit as a merge request to
                        https://gitlab.com/radiobrowser/radio-database under src/us/.
  new-stations.json     Stations not on RadioBrowser yet. The GitLab repo can't add
                        stations, so enter these at https://www.radio-browser.info/add,
                        then record the new UUIDs in stations.json.

Field set and order match the repo README; its CI rejects extra or missing fields.
"""
import json
from pathlib import Path

root = Path(__file__).resolve().parent
data = json.loads((root / "stations.json").read_text())
base = data["base_url"].rstrip("/") + "/"
LANG = {"english": "EN", "spanish": "ES"}


def entry(s, with_uuid):
    e = {}
    if with_uuid:
        e["stationuuid"] = s["radiobrowser"]
    e.update({
        "name": s["radiobrowser_name"],
        "url": s["stream"],
        "homepage": s["homepage"],
        "favicon": base + s["logo"],
        "tags": ",".join(s.get("tags", [])),
        "countrycode": s["country"],
        "iso_3166_2": s["iso_3166_2"],
        "languagecodes": LANG.get(s["language"], s["language"][:2].upper()),
        "geo_lat": s["geo_lat"],
        "geo_long": s["geo_long"],
    })
    return e


existing = [entry(s, True) for s in data["stations"] if s.get("radiobrowser")]
new = [entry(s, False) for s in data["stations"] if not s.get("radiobrowser")]

out = root / "radiobrowser-export"
out.mkdir(exist_ok=True)
(out / "update-existing.json").write_text(json.dumps(existing, indent=2, ensure_ascii=False) + "\n")
(out / "new-stations.json").write_text(json.dumps(new, indent=2, ensure_ascii=False) + "\n")
print(f"update-existing.json: {len(existing)} stations; new-stations.json: {len(new)} stations")
