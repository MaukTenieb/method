# Prose, checks, search engines

French summary in [README.md](README.md).

## Prose and checks

### A linter for machine-written prose

Obstacle. Public texts carried the tics of AI writing, in English and French.

Technique. Families of patterns from Wikipedia's "Signs of AI writing" and the house rules: puffery, trailing participles, "not X but Y", triads, vague attributions, signposting, chat residue, spaced dashes, lists of bold labels, runs of eight mid-length sentences. Exit code 1 on a hit; a weekly workflow commits the report.

Code. [method/prose/prose-lint.py](../prose/prose-lint.py), [prose/RULES.md](../prose/RULES.md).

### One check across every public repository

Obstacle. Rights lines, retired names and dead links drift across fifteen repositories.

Technique. List the repositories through the API, read each README and page. Before the link test, strip markdown marks glued to addresses (`**`): they made false dead links. Placeholder links stay out, and so does the check's own list of retired names.

Code. [method/coherence/check.py](../coherence/check.py).

### A voice measured in numbers

Obstacle. A translation keeps the rhythm of the author's French.

Technique. Measure a reference corpus: mean sentence length, share of sentences of 4 words or fewer and of 30 or more, brackets, semicolons, dashes and ellipses per 1 000 words, slang; store percentile bands, and score the translation against them. The repository keeps the numbers and the rules, zero text of the corpus.

### Every removal accounted for

Technique. In a bulk cleaning, each link of the original absent from the output falls into a named class of removal: zero unexplained out of 336. Cleaning touches the text between addresses only: split on `https?://\S+` and edit the even pieces.

## Search engines

### One entity, told apart

Obstacle. A search for the site's names returned a Kotlin library and an Ivorian city.

Technique. In JSON-LD, `disambiguatingDescription` names the neighbours (the io.insert-koin library, the cloth and the city of Korhogo); one identical `sameAs` list on every site; the same text in `llms.txt`.

Code. [insertkoin/index.html](https://github.com/MaukTenieb/insertkoin/blob/main/index.html), JSON-LD.

### Answer engines in, training crawlers out

Technique. `robots.txt` lets in OAI-SearchBot, ChatGPT-User, PerplexityBot, Claude-SearchBot and Claude-User, and shuts out GPTBot, Google-Extended, CCBot, ClaudeBot, anthropic-ai, Applebot-Extended, Bytespider and meta-externalagent. `.well-known/tdmrep.json` (W3C TDMRep) states the reservation; on Pages, `_config.yml` holds `include: [".well-known"]`, since Jekyll skips dot folders.

Code. [mauktenieb.github.io/robots.txt](https://github.com/MaukTenieb/mauktenieb.github.io/blob/main/robots.txt), [_config.yml](https://github.com/MaukTenieb/mauktenieb.github.io/blob/main/_config.yml).

### IndexNow for a whole Pages domain

Obstacle. New pages wait weeks for Bing, which also feeds ChatGPT Search and Copilot.

Technique. The key file at the root. A workflow (on push, each Monday, by hand) waits 120 s for Pages to publish the key, gathers the addresses of every sitemap, builds the body with jq (`host`, `key`, `keyLocation`, `urlList`) and POSTs it to `api.indexnow.org/indexnow`.

Code. [mauktenieb.github.io/.github/workflows/indexnow.yml](https://github.com/MaukTenieb/mauktenieb.github.io/blob/main/.github/workflows/indexnow.yml).

### One Search Console property for every project site

Technique. One URL-prefix property, `https://user.github.io/`, covers every sub-path; a meta tag in the root `index.html` verifies it. Bing: the site added by hand, with a `msvalidate.01` meta tag.

### Blocks written again in place

Obstacle. Repeated passes stacked copies of the same block in pages and READMEs.

Technique. Each generated block sits between markers (`<!--seo-->…<!--/seo-->`, `<!-- network:start -->…<!-- network:end -->`); a new pass replaces what lies between them. Redirect stubs and 404 pages take `noindex`; the author's own title, description or canonical stays.

Code. [alchimie-delboy/scripts/16_seo.py](https://github.com/MaukTenieb/alchimie-delboy/blob/main/scripts/16_seo.py).
