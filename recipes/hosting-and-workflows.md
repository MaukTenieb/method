# Hosting and workflows

GitHub Pages, service workers, GitHub Actions. French summary in [README.md](README.md).

## Hosting

### Network first for code, cache first for assets

Obstacle. A returning visitor kept a stale script from the service worker: the fixed FaunaTor still failed for him.

Technique. In the `fetch` handler, navigations and html, js, css, json, txt and md files go to the network first (`cache.put` on success, cache when offline); images, fonts and wasm come from the cache and refresh in the background. On `activate`, every cache other than the current one goes; then `skipWaiting()` and `clients.claim()`.

Code. [insertkoin/sw.js](https://github.com/MaukTenieb/insertkoin/blob/main/sw.js), commit [a60ec1c](https://github.com/MaukTenieb/insertkoin/commit/a60ec1c).

### A cache name stamped at each release

Obstacle. After a release, visitors kept the old code and an old sprite sheet.

Technique. `sw.js`, line 2: `const C='ik-YYYYMMDDHHMM'`, rewritten at each release by `sed -E "s/ik-[0-9]{12}/ik-$(date -u +%Y%m%d%H%M)/"`. A replaced image takes `?v=YYYYMMDD` in its address.

Code. [insertkoin/sw.js](https://github.com/MaukTenieb/insertkoin/blob/main/sw.js), commit [16fe10c](https://github.com/MaukTenieb/insertkoin/commit/16fe10c).

### Testing a release on Pages

Obstacle. A site looks unchanged right after a push.

Technique. Pages keeps each file about ten minutes at the edge, and an old service worker leaves at the second load. Test in a private window, or wait and reload with Ctrl+Shift+R.

### robots.txt counts at the domain root only

Obstacle. A `robots.txt` in `user.github.io/<project>/` stays unread by crawlers.

Technique. The user site, repo `user.github.io`, holds the one `robots.txt` of the domain: the rules, and one `Sitemap:` line per project site.

Code. [mauktenieb.github.io/robots.txt](https://github.com/MaukTenieb/mauktenieb.github.io/blob/main/robots.txt).

### Short links on Pages

Obstacle. Share addresses (`?k=` and a 64-hex key) run long, and outside shorteners close.

Technique. The root site's `404.html` (noindex) reads `location.pathname`, matches `/k/<8 to 64 hex>` and calls `location.replace('/insertkoin/?k=' + key)`. The page looks the cassette up by key prefix.

Code. [mauktenieb.github.io/404.html](https://github.com/MaukTenieb/mauktenieb.github.io/blob/main/404.html) · [insertkoin/ik-kuration.js](https://github.com/MaukTenieb/insertkoin/blob/main/ik-kuration.js).

### One source page, the other language generated

Obstacle. `index.html` and `fr.html`, two copies of 188 KB, drifted apart.

Technique. `build-fr.py` writes `fr.html` from `index.html` with exact string pairs; `fr.html` stays out of hand editing. Release routine: `build-fr.py`, `node --check` on each extracted `<script>`, new cache name, `git pull --rebase`, push.

Code. [insertkoin/build-fr.py](https://github.com/MaukTenieb/insertkoin/blob/main/build-fr.py).

### A heavy repository on a light disk

Obstacle. A site of 4 700 files and 130 MB of images fills a small working disk.

Technique. `git clone --filter=blob:none --sparse`, then `git sparse-checkout set` on the folders at work; `git add -A --sparse` stages the changes; `git -c http.postBuffer=524288000 push` sends the large files.

Code. Used on [alchimie-delboy](https://github.com/MaukTenieb/alchimie-delboy).

### Zero cost, with a hard stop

Obstacle. Private Actions minutes approach the free 2 000 a month.

Technique. Budgets at 0 $ per product with "Stop usage when budget limit is reached" (Actions, Packages, Git LFS, Codespaces); public repositories run Actions free. Minutes of a period: page through `repos/<r>/actions/runs?per_page=100&created=>=DATE` and add `updated_at − run_started_at`, each rounded up to the minute.

## Workflows

### The answer of a job on a branch

Obstacle. Job logs stay out of reach of the session that asked.

Technique. The job writes its result in `/tmp`, runs `git init`, commits and pushes to a `result` branch with `x-access-token:${{ github.token }}`. The reader runs `git fetch origin result` and `git show origin/result:results.md`. To keep a history: `git fetch origin result && git reset --soft origin/result` before the commit.

Code. [reporhogo/.github/workflows/search.yml](https://github.com/MaukTenieb/reporhogo/blob/main/.github/workflows/search.yml) · [Korhoname](https://github.com/MaukTenieb/Korhoname) · [insertkoin vhs-probe.yml](https://github.com/MaukTenieb/insertkoin/blob/main/.github/workflows/vhs-probe.yml).

### A request is a line in a file

Obstacle. A tool should run on demand, from any device, through a one-line file.

Technique. `on: push: branches: [main], paths: ['queue.txt']`; the job reads `grep -v '^#' queue.txt`. A request is a one-line commit; the answer lands on the `result` branch.

Code. [reporhogo/queue.txt](https://github.com/MaukTenieb/reporhogo/blob/main/queue.txt) · [Korhoname](https://github.com/MaukTenieb/Korhoname).

### The log of a failed job

Obstacle. A failed step ends the job before the push, and its cause stays unknown.

Technique. `exec > >(tee log.txt) 2>&1`, or `cmd | tee log.txt || true`: the next step still commits `log.txt` to the result branch.

Code. [detour/.github/workflows/catchlight-test.yml](https://github.com/MaukTenieb/detour/blob/main/.github/workflows/catchlight-test.yml).

### Dispatch and cancel by REST

Technique. Dispatch: `gh api -X POST repos/O/R/actions/workflows/F.yml/dispatches -f ref=main -f "inputs[x]=…"`. Cancel: `…/actions/runs/ID/cancel`, then `force-cancel`; `jobs[0].steps` shows which steps ran.

### workflow_run takes the workflow's name

Obstacle. A chained workflow stays idle.

Technique. `on: workflow_run: workflows: ['YouTube canon apply']` names the `name:` field of the first workflow, its file name aside.

### A Cloudflare Worker deployed from Git

Obstacle. Daily commits of a bot redeployed the Worker, and the dashboard settings drifted from the repository.

Technique. Repository connected through Settings, Builds (`npx wrangler deploy`); `wrangler.toml` copies the live `[vars]`; bot commits carry `[skip ci]`.

Code. [korhotube/wrangler.toml](https://github.com/MaukTenieb/korhotube/blob/main/wrangler.toml).

### Rust to WebAssembly in Actions

Obstacle. The working session lacks a Rust and WebAssembly toolchain.

Technique. In the workflow: `rustup target add wasm32-unknown-unknown`, `npm i -g wasm-pack@0.15.0`, build, commit the `.js` and `.wasm` files under a bot identity, `git pull --rebase` before the push.

Code. [insertkoin/.github/workflows/faunator-tor.yml](https://github.com/MaukTenieb/insertkoin/blob/main/.github/workflows/faunator-tor.yml).

### MediaPipe on an Ubuntu runner

Obstacle. MediaPipe Face Mesh crashes on the Linux runner.

Technique. `sudo apt-get install -y libegl1 libgles2`; `mediapipe==0.10.14`, the last version with the refined iris model.

Code. [detour/.github/workflows/catchlight-test.yml](https://github.com/MaukTenieb/detour/blob/main/.github/workflows/catchlight-test.yml).
