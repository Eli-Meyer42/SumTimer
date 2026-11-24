# Sum Timer

Voice-driven enemy summoner spell and objective timers for League of Legends.
Live at **https://eli-meyer42.github.io/SumTimer/**

| File | What it is |
|---|---|
| `index.html` | The whole app. |
| `manifest.webmanifest` | Makes it installable with its own icon. Paths are relative (Pages serves from `/SumTimer/`). |
| `sw.js` | Service worker. Network-first for the page, so deploys show up immediately. |
| `make-icons.py` | Regenerates the icons. `python3 make-icons.py` |
| `icon-*.png` | App icons. |

- Hosting: GitHub Pages, `main` branch, `/ (root)`. Every push redeploys.
- Data: game logs sync through Firebase Realtime Database at `sumtimer/main` (one node per device).
- Activity log: sent to the private repo `Eli-Meyer42/shopping-logs` under `sumtimer/logs/<device>/`.
- Bump the build stamp (`APP.build` in `index.html`) on every push.
