# Browser and tests

Canvas games, touch, embeds, files made in the page; tests offline. French summary in [README.md](README.md).

## In the browser

### A YouTube frame behind a drawn object

Obstacle. A YouTube clip on the TV of a game covered the table drawn in front of it.

Technique. Draw the foreground layer into a mask canvas with `globalCompositeOperation = 'destination-out'`, then set it as the frame's CSS mask: `maskImage = url(canvas.toDataURL())`, `maskSize: 100% 100%`.

Code. [insertkoin/index.html](https://github.com/MaukTenieb/insertkoin/blob/main/index.html) (`tvClip`), commit [c523a99](https://github.com/MaukTenieb/insertkoin/commit/c523a99).

### A letterboxed canvas in fullscreen

Obstacle. On 20:9 phones in fullscreen, the game stretched and lost its bottom.

Technique. `.stage:fullscreen canvas { width: min(100vw, calc(100vh*512/343)); height: min(100vh, calc(100vw*343/512)) }`. The overlays take their place from the canvas's real bounding rectangle.

Code. [insertkoin/index.html](https://github.com/MaukTenieb/insertkoin/blob/main/index.html), commit [157553d](https://github.com/MaukTenieb/insertkoin/commit/157553d).

### A touch paddle like a trackpad

Obstacle. The paddle jumped under the finger; pulling back met the Android gesture edge; a finger slid off the screen sent zero lift, and the game froze on two fingers.

Technique. Relative drag from the first touch, with a gain of ×1.7 across and ×2.2 in depth, on coalesced events. A primary `pointerdown` clears stale ids (`if (e.isPrimary) TOUCH.clear()`); `lostpointercapture` and `pointercancel` count as a lift; the gain allows for the letterbox bars.

Code. [insertkoin/index.html](https://github.com/MaukTenieb/insertkoin/blob/main/index.html), commits [47978cb](https://github.com/MaukTenieb/insertkoin/commit/47978cb), [0327097](https://github.com/MaukTenieb/insertkoin/commit/0327097).

### The mouse held during play

Technique. `requestPointerLock({ unadjustedMovement: false })`, skipped when `matchMedia('(pointer: coarse)')` matches; released on Enter and at the end of the match.

Code. [insertkoin/index.html](https://github.com/MaukTenieb/insertkoin/blob/main/index.html) (`lockIn`).

### YouTube embeds free of cookies

Obstacle. Embeds raise the question of a consent banner.

Technique. `host: 'https://www.youtube-nocookie.com'` in `new YT.Player`, and nocookie embed addresses; `www.youtube.com` serves the `iframe_api` script only.

Code. [insertkoin/kg-vhs.js](https://github.com/MaukTenieb/insertkoin/blob/main/kg-vhs.js).

### One balance for two sites of one origin

Obstacle. The arcade and the Minitel, two project sites on one origin, share a live balance of Koins.

Technique. Keys `ik.*` in localStorage, a `storage` listener for the other tabs, a 1.5 s poll for the same tab.

Code. [insertkoin/index.html](https://github.com/MaukTenieb/insertkoin/blob/main/index.html) (`syncKoins`).

### Files written in the page, zero library

Obstacle. XLSX and EPUB are ZIP files.

Technique. A ZIP in stored mode, by hand: CRC-32 table, local headers, central directory, about 30 lines. XLSX needs five OOXML parts; EPUB needs `mimetype` first and XHTML free of Word tags.

Code. [insertkoin/kg-vhs-recorder.js](https://github.com/MaukTenieb/insertkoin/blob/main/kg-vhs-recorder.js) (`crc32`) · [alchimie-delboy/site/barre.js](https://github.com/MaukTenieb/alchimie-delboy/blob/main/site/barre.js) (`zip`).

### Saved files named in the Republican calendar

Obstacle. Dates slipped by one day at the change to winter time.

Technique. Count from the visitor's local calendar day, apart from milliseconds divided by 86 400 000. Years III, VII, XI and XV are sextile; from year XX, Romme's rule applies. Names: `day-month-year_program_NNN`, with a counter per day in localStorage.

Code. [insertkoin/ik-name.js](https://github.com/MaukTenieb/insertkoin/blob/main/ik-name.js).

### Names sorted by their rendered width

Obstacle. A list runs from the widest name to the narrowest, as each platform draws it; a count of characters gets it wrong.

Technique. In the page: `canvas.measureText` in the font of `getComputedStyle`, then a sort. Offline: `npm pack @fontsource/<font>`, widths from fontTools (`hmtx / unitsPerEm × px`), and the `cmap` table to spot glyphs that fall back to another font.

## Tests

### A game closed in a function

Obstacle. Playwright reaches zero state of a game wrapped in an IIFE.

Technique. A local copy of the page, kept out of the repository, sets `window.__k = { R, start, G }` before the function closes. `python3 -m http.server` serves it, Playwright drives it, PIL builds contact sheets.

### YouTube, APIs and fonts replaced in the test browser

Technique. `add_init_script` installs a fake `window.YT.Player` that records `cueVideoById`, `loadVideoById` and `stopVideo`. `page.route('https://musicbrainz.org/ws/2/**')` answers with recorded data; the same route swaps Google Fonts for @fontsource files. `--use-gl=swiftshader` gives WebGL to headless Chromium.

### Difficulty measured on a bench

Obstacle. The difficulty of each opponent needs thousands of matches.

Technique. Extract the engine and the roster from the inline `<script>`, evaluate them in Node, fire thousands of slow, medium and fast pucks per opponent, and bisect the error parameter to a target miss rate.

### Real touch events

Obstacle. A bug of Android in landscape stays hidden under mouse emulation.

Technique. `Input.dispatchTouchEvent` through a Playwright CDP session, in a Pixel 8 viewport (915 × 380).

### The live site seen from a runner

Obstacle. The working session has zero access to the live site and the relays.

Technique. A workflow opens the published site with Playwright on the GitHub runner and commits a report: visible text, console errors, failed requests, a screenshot at 412 × 900.

Code. [insertkoin/.github/workflows/vhs-probe.yml](https://github.com/MaukTenieb/insertkoin/blob/main/.github/workflows/vhs-probe.yml).

### Network scripts run offline

Technique. The Nostr routine runs under `node --import` with a fake `WebSocket` class; inline scripts pass `node --check` or `new Function(src)`. Archive clients run on recorded answers: [reporhogo/captures/test_captures.py](https://github.com/MaukTenieb/reporhogo/blob/main/captures/test_captures.py).
