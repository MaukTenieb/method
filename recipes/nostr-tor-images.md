# Nostr, Tor, images

French summary in [README.md](README.md).

## Nostr

### A scoreboard with zero server

Obstacle. A leaderboard, and zero database.

Technique. Each browser signs a kind 30078 event (NIP-78, tag `d` per game and run); relays keep the last version per key and `d`. Every hour, a job sends `REQ {kinds, #t, since}` to four relays and keeps the events that pass `verifyEvent`. One rules file, shared by the page and the job, rejects impossible scores. `palmares.json` changes only when its content changes, `updated` and `relays` aside.

Code. [insertkoin/tools/palmares.mjs](https://github.com/MaukTenieb/insertkoin/blob/main/tools/palmares.mjs), [palmares-rules.js](https://github.com/MaukTenieb/insertkoin/blob/main/palmares-rules.js), [.github/workflows/palmares.yml](https://github.com/MaukTenieb/insertkoin/blob/main/.github/workflows/palmares.yml).

### Proof of work against spam

Obstacle. Spam reached the Minitel mailbox; zero server filters it, and a CAPTCHA stays out.

Technique. `NT.nip13.minePow(tpl, 16)` on kinds 4 and 42 before signing: 0.3 to 0.8 s in a browser. On receipt, events under `getPow(ev.id) < 16` drop; older events pass from known keys only.

Code. [3615/index.html](https://github.com/MaukTenieb/3615/blob/main/index.html).

### Imported keys keep quiet

Technique. The flag `vdx.nostr.own = 1` marks the keys made in this browser; they alone publish a kind 0 profile. An imported or test key leaves the real profile intact.

## Tor

### A Tor client in the page

Obstacle. Reading `.onion` and blocked sites, with zero extension and zero server.

Technique. Two WebAssembly builds of webtor-rs: privacy-ethereum v0.5.7 for the clear web, andrewtheguy v0.0.1-alpha.25 for onion v3 over http. They reach Tor through Snowflake, WebSocket bridges first, brokered WebRTC last. Each failure carries its reason.

Code. [insertkoin/tor-web.js](https://github.com/MaukTenieb/insertkoin/blob/main/tor-web.js), [tor-onion.js](https://github.com/MaukTenieb/insertkoin/blob/main/tor-onion.js), [faunator-tor.js](https://github.com/MaukTenieb/insertkoin/blob/main/faunator-tor.js) · [FaunaTor](https://github.com/MaukTenieb/faunator).

### The consensus on the same origin

Obstacle. The host of the Tor consensus refuses CORS; the client in the page fails to start.

Technique. A workflow (`23 5,17 * * *`) runs `scripts/fetch-consensus.sh` of webtor-rs and commits `consensus.txt.br` and `microdescriptors.txt.br` under `tor/`; the client reads them there.

Code. [insertkoin/.github/workflows/tor-consensus.yml](https://github.com/MaukTenieb/insertkoin/blob/main/.github/workflows/tor-consensus.yml).

### A race, and the real reason of a failure

Technique. A custom `any([...])` races public relays against Tor, then a reader, and keeps the last real error. The onion directory stays 2.5 to 3 h in IndexedDB. Images and CSS of an onion page come through Tor and go inline (16 images, 2 MB at most); the page shows in a sandboxed frame, scripts removed.

Code. [insertkoin/tor.html](https://github.com/MaukTenieb/insertkoin/blob/main/tor.html).

## Images

### Background removal by a two-to-one vote

Obstacle. Matting networks, trained on people, drop wings, clouds and props, and keep painted walls.

Technique. Per pixel, U²-Net and IS-Net (ONNX weights of the rembg releases) and a measure of distance to the backdrop vote; two votes against one decide. A rescue rule returns textured regions attached to the figure (Laplacian over twice the backdrop level), table shapes apart.

Code. [detour/detour.py](https://github.com/MaukTenieb/detour/blob/main/detour.py), `decide()`, `judge_panel()`, `neural()`.

### A smooth painted backdrop

Obstacle. Gradients and vignettes defeat a flat colour key.

Technique. Per LAB channel, a least-squares polynomial in x and y (1, x, y, xy, x², y², y³) fitted on the border, or where both networks agree. Five passes reject residuals over 3σ (robust σ = 1.48 × median); distances count in noise units.

Code. [detour/detour.py](https://github.com/MaukTenieb/detour/blob/main/detour.py), `backdrop()`.

### Clean edges at the final size

Obstacle. Enlarged masks look jagged; blur softens the ink; a 2 × 2 opening in OpenCV shifts the mask by one pixel.

Technique. Mask to signed distance field, smoothing under one pixel, resize, threshold with 1 px of antialiasing. Colours just outside the figure get inpainted (`cv2.INPAINT_TELEA`), so the soft edge shows zero backdrop. `open2`: erode with anchor (0, 0), dilate with anchor (1, 1).

Code. [detour/detour.py](https://github.com/MaukTenieb/detour/blob/main/detour.py), `render()`, `open2()`.

### Hands on a table, floor between legs

Technique. Find the top line of the table; below it, keep what differs from the wood, sampled column by column; fit the wall model above the table only. An enclosed pocket goes when it matches the local backdrop hue: a beige hoof reads warmer than a beige floor.

Code. [detour/detour.py](https://github.com/MaukTenieb/detour/blob/main/detour.py), `table_hands()`, `remove_pockets()`.

### Light in the eyes, frame by frame, under test

Obstacle. Highlights placed by hand drift across the eight expressions of a sheet.

Technique. MediaPipe Face Mesh: iris points 468 and 473 and the eyelids say open or shut per frame; `matchTemplate` (`TM_CCOEFF_NORMED`) refines the place. The CI compares the result with `catchlights.json`: within 2 cell units, one lit or dark disagreement at most in 32 frames.

Code. [detour/catchlight.py](https://github.com/MaukTenieb/detour/blob/main/catchlight.py), [catchlight-test.yml](https://github.com/MaukTenieb/detour/blob/main/.github/workflows/catchlight-test.yml).

### Character sheets of equal frames

Technique. In Midjourney, `--chaos 0` keeps one character across the cells; `--ar 134:59` gives a grid of 4 × 2 cells of 67:59, the 536 × 472 px frame of the game; plain backgrounds, full figure inside the frame.
