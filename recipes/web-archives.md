# Web archives and old sites

Recipes from the recovery of Hervé Delboy's site on alchemy (two hosts, 1999–2016) and from [Captures](https://github.com/MaukTenieb/reporhogo/tree/main/captures), the archive tool of Reporhogo. French summary in [README.md](README.md).

### An error page served with the code 200

Obstacle. Club-Internet answered a dead page with its error page and the code 200. The Wayback Machine kept these error pages as valid captures: 46 links of the site led to them.

Technique. Group the captures by digest. One digest under three addresses or more marks the host's error page; the download skips it. A size band (6 900 to 7 000 bytes for Club-Internet in 2002) confirms it.

Code. [captures.py](https://github.com/MaukTenieb/reporhogo/blob/main/captures/captures.py), `shared_digests()` · [alchimie-delboy/scripts/09_recover.py](https://github.com/MaukTenieb/alchimie-delboy/blob/main/scripts/09_recover.py), `ERR_BAND`.

### The digest filter hides captures

Obstacle. The CDX option `collapse=digest` keeps one capture per content. A page whose first capture holds the error page then shows a single, empty capture, and its later good captures drop out of the list.

Technique. Query the index without `collapse`, with every status, and page through it with `showResumeKey=true` and `resumeKey`. On a whole site, slice the query year by year (`from`, `to`): each slice stays small and answers fast.

Code. [captures.py](https://github.com/MaukTenieb/reporhogo/blob/main/captures/captures.py), `wayback()` · first inventory with `collapse`: [alchimie-delboy/scripts/01_inventory.py](https://github.com/MaukTenieb/alchimie-delboy/blob/main/scripts/01_inventory.py).

### File names absent from every link

Obstacle. A page moves inside a site, or keeps a name that no link quotes.

Technique. `matchType=prefix` on the site lists every address ever captured under it. A pattern on the file name (`--name`) then finds the moved pages. Common Crawl and Arquivo.pt accept the same prefix query; Common Crawl has one index per crawl since 2008.

Code. [captures.py](https://github.com/MaukTenieb/reporhogo/blob/main/captures/captures.py), `run()`, `commoncrawl()`, `arquivo()`.

### One page, many spellings

Obstacle. The archives index the address as each crawler met it: `http` or `https`, `www` or bare host, `.htm` or `.html`, capitals, spaces as `%20` or `+`, two hosts for the same site.

Technique. Send every variant: `variants()` builds them from one address and the other hosts of the site (`--alias`).

Code. [captures.py](https://github.com/MaukTenieb/reporhogo/blob/main/captures/captures.py), `variants()`.

### The page as the archive received it

Obstacle. The Wayback Machine wraps each page in its toolbar and rewrites its links.

Technique. `web.archive.org/web/<timestamp>id_/<address>`: the suffix `id_` returns the original bytes. Arquivo.pt and other pywb archives accept the same suffix.

Code. [alchimie-delboy/scripts/02_fetch_pages.py](https://github.com/MaukTenieb/alchimie-delboy/blob/main/scripts/02_fetch_pages.py) · [captures.py](https://github.com/MaukTenieb/reporhogo/blob/main/captures/captures.py).

### One Common Crawl page, by byte range

Obstacle. A Common Crawl WARC file weighs about a gigabyte.

Technique. The index gives `filename`, `offset` and `length`. An HTTP `Range` request on `https://data.commoncrawl.org/<filename>` returns one gzip member: the WARC headers, the HTTP headers, then the page.

Code. [captures.py](https://github.com/MaukTenieb/reporhogo/blob/main/captures/captures.py), `cc_fetch()`.

### Every other archive in one query

Obstacle. National and university archives each have their own interface.

Technique. The Memento protocol (RFC 7089) gives each archive the same timemap in link format: `<uri>; rel="memento"; datetime="…"`. Memento Time Travel aggregates them in one query; the Library of Congress, the UK Web Archive and archive.today answer it directly.

Code. [captures.py](https://github.com/MaukTenieb/reporhogo/blob/main/captures/captures.py), `TIMEMAPS`, `parse_timemap()`.

### ISO-8859-1 declared, cp1252 written

Obstacle. French pages of the 2000s declare ISO-8859-1 and contain bytes 0x80–0x9F from Windows: œ, ’, « », –. A latin-1 decoder turns them into control characters.

Technique. Decode in latin-1, then map the 27 defined positions 0x80–0x9F to their cp1252 characters and keep the 5 undefined bytes as they are.

Code. [alchimie-delboy/scripts/common.py](https://github.com/MaukTenieb/alchimie-delboy/blob/main/scripts/common.py), `decode_html()`.

### A reading bar over pages kept as written

Obstacle. The author's pages carry their own layout, tables and fonts; a site stylesheet breaks them.

Technique. Keep each page byte for byte, add two links (`barre.css`, `barre.js`), and let the script wrap the body in one element (`#dlb-page`). Zoom, night mode, black and white and the magnifier act on that element only; `nav.json` gives the author's order for previous and next.

Code. [alchimie-delboy/site/barre.js](https://github.com/MaukTenieb/alchimie-delboy/blob/main/site/barre.js) · [scripts/13_lecture.py](https://github.com/MaukTenieb/alchimie-delboy/blob/main/scripts/13_lecture.py).

### A link to a passage

Obstacle. Text fragments (`#:~:text=`) depend on the browser and escape headless tests.

Technique. A hash `#passage=<words>`: the page script searches the words in the text nodes, wraps them in `<mark>` and scrolls to them. A search result links straight to the passage.

Code. [alchimie-delboy/site/barre.js](https://github.com/MaukTenieb/alchimie-delboy/blob/main/site/barre.js), block `#passage=`.

### An EPUB built in the browser

Obstacle. EPUB requires a ZIP whose first entry, `mimetype`, stays uncompressed; old HTML exported from Word holds `o:p` tags and prefixed attributes, invalid in XHTML.

Technique. Write the ZIP by hand in stored mode (CRC-32 table, local headers, central directory): 30 lines, zero library. Strip namespace-prefixed tags and attributes before the XHTML serialisation.

Code. [alchimie-delboy/site/barre.js](https://github.com/MaukTenieb/alchimie-delboy/blob/main/site/barre.js), `crc32()`, `zip()`.

### Books printed from the pages themselves

Obstacle. A PDF rebuilt from extracted text loses the author's layout.

Technique. Chromium prints each page (`page.pdf`, footer template with the title and the capture date); pypdf merges them and adds one bookmark per page. The cover lists the first page of each piece: print it, count its pages, number again, up to a stable count.

Code. [alchimie-delboy/scripts/15_pdf.py](https://github.com/MaukTenieb/alchimie-delboy/blob/main/scripts/15_pdf.py).

### Full-text search on static hosting

Obstacle. A 43 MB index exceeds what a phone loads for one query.

Technique. Split the vocabulary into shards by first letters; a query loads the shards of its terms, ranks with BM25, then loads the passages shown. 20 to 300 ms.

Code. [alchimie-delboy/scripts/07_build_index.py](https://github.com/MaukTenieb/alchimie-delboy/blob/main/scripts/07_build_index.py), `shard_of()`.
