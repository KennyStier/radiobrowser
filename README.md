# Radio Streams

Working stream URLs and square 512×512 logos for a few radio stations, hosted on GitHub Pages so the logos have permanent public URLs for Music Assistant, RadioBrowser and other players.

**Site:** https://kennystier.github.io/radiobrowser/

| Station | Stream |
|---|---|
| 92.3 WTTS | `https://playerservices.streamtheworld.com/api/livestream-redirect/WTTSAAC.aac` |
| Sacred Heart Catholic Radio (WNOP 740 AM) | `https://ice10.securenetsystems.net/WNOP2` |
| Tree Country 1330 (WTRE) | `https://wtre.streamguys1.com/live` |
| Ave Maria Radio | `https://streaming.live365.com/a57262` |

## Adding a station

1. Put a square PNG logo (512×512 is ideal) in `logos/`.
2. Add an entry to `stations.json`.
3. Run `python3 build.py` to regenerate `radio.m3u`.
4. Commit and push. Pages updates in a minute or two.

## Notes

- StreamTheWorld stations: use the `playerservices.streamtheworld.com/api/livestream-redirect/<MOUNT>.aac` form. Numbered relay hosts (`12345.live.streamtheworld.com`) change and start returning 403.
- Logos belong to their stations and are used here only to identify them.
