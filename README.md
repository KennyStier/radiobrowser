# Radio Streams

Working stream URLs and square 512×512 logos for a few radio stations, hosted on GitHub Pages so the logos have permanent public URLs for Music Assistant, RadioBrowser and other players.

**Site:** https://kennystier.github.io/radiobrowser/

| Station | Stream |
|---|---|
| 92.3 WTTS | `https://playerservices.streamtheworld.com/api/livestream-redirect/WTTSAAC.aac` |
| Sacred Heart Catholic Radio (WNOP 740 AM) | `https://ice10.securenetsystems.net/WNOP2` |
| Tree Country 1330 (WTRE) | `https://wtre.streamguys1.com/live` |
| Ave Maria Radio | `https://streaming.live365.com/a57262` |
| WBAA Classical | `https://wfyi-live.streamguys1.com/wbaa-classical-aac` |
| WBAA Jazz | `https://wfyi-live.streamguys1.com/wbaa-jazz-aac` |
| WIBC 93.1 FM | `https://playerservices.streamtheworld.com/api/livestream-redirect/WIBCFM.mp3` |
| 106.1 The River (WWWY) | `https://live.amperwave.net/direct/findlay-wwwyfmmp3-ibc3` |
| WRBI 103.9 FM | `https://ice41.securenetsystems.net/WRBI` |

## Adding a station

1. Put a square PNG logo (512×512 is ideal) in `logos/`.
2. Add an entry to `stations.json`. If the station is listed on [RadioBrowser](https://www.radio-browser.info), put its station UUID in `radiobrowser` and the page will link to it.
3. Run `python3 build.py` to regenerate `radio.m3u`.
4. Commit and push. Pages updates in a minute or two.

## Notes

- StreamTheWorld stations: use the `playerservices.streamtheworld.com/api/livestream-redirect/<MOUNT>.aac` form. Numbered relay hosts (`12345.live.streamtheworld.com`) change and start returning 403.
- Logos belong to their stations and are used here only to identify them.

## Submitting to RadioBrowser

Run `python3 export_radiobrowser.py`. It writes two files to `radiobrowser-export/`:

- `update-existing.json`: stations already on RadioBrowser. Add it as `src/us/<name>.json` in a merge request to [radiobrowser/radio-database](https://gitlab.com/radiobrowser/radio-database). Its CI requires exactly these fields, so don't add or remove any.
- `new-stations.json`: stations not on RadioBrowser yet. The GitLab repo can only change or delete existing stations, so add these at <https://www.radio-browser.info/add>, then put each new UUID in `radiobrowser` in `stations.json`.

Coordinates are the city of license (Ave Maria Radio: its Ann Arbor studios), from OpenStreetMap, to 4 decimal places.
