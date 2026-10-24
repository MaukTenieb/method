# Reconstitute a website from the web archives

The general procedure, drawn from the recovery of Hervé Delboy's site ([recover-a-lost-website.md](recover-a-lost-website.md)). Tools: [Captures](https://github.com/MaukTenieb/reporhogo/tree/main/captures) for the archives, [Reporhogo](https://github.com/MaukTenieb/reporhogo) for the code forges. Directory of the archives: [archives/](../archives/README.md). French below.

## Who does what

| step | who |
|---|---|
| the site to reconstitute, its scope, the texts written for it | the owner of the project |
| searches, code, reading, publication, checks, report | the assistant |
| a tool against a source closed to the assistant | the owner: one button in GitHub Actions; or the assistant on the owner's computer |
| a page behind a CAPTCHA | a person, in a browser |
| an archive on site or on request (BnF, national libraries) | a person, by visit or by letter |

## 1. Read what others wrote

Before any code, Reporhogo searches the forges, and the IIPC list [awesome-web-archiving](https://github.com/iipc/awesome-web-archiving) gives the reference tools. Their code and their test data get read.

| tool | use | language, licence | last commit read |
|---|---|---|---|
| [StrawberryMaster/wayback-machine-downloader](https://github.com/StrawberryMaster/wayback-machine-downloader) | every file of a site from the Wayback Machine: time range, every timestamp, exact address, file filter, concurrency, local links | Ruby, MIT | 2026-10-17 |
| [jsvine/waybackpack](https://github.com/jsvine/waybackpack) | every capture of one address, raw (`--raw`), dates, `--uniques-only`, retries | Python, MIT | 2025-04-20 |
| [cocrawler/cdx_toolkit](https://github.com/cocrawler/cdx_toolkit) | one interface for the indexes of Common Crawl and the Internet Archive; WARC extracts of a subset | Python, Apache 2.0 | 2026-09-07 |
| [karust/gogetcrawl](https://github.com/karust/gogetcrawl) | addresses and files from the Wayback Machine and Common Crawl, several domains, workers | Go, MIT | 2026-10-22 |
| [wabarc/playback](https://github.com/wabarc/playback) | one page searched in the Internet Archive, archive.today, Memento and others | Go, GPL 3.0 | 2026-04-12 |
| [oduwsdl/MemGator](https://github.com/oduwsdl/MemGator) | Memento aggregator, command line and server; its archive list feeds Captures | Go, MIT | 2026-04-09 |
| [nabertronic/pastpage](https://github.com/nabertronic/pastpage) | browser extension: a broken page searched in several archives at once | JavaScript, MIT | 2026-10-19 |
| [httpreserve/linkstat](https://github.com/httpreserve/linkstat) | status of a page, its first and last capture | Go, GPL 3.0 | 2026-07-05 |
| [webrecorder/warcio](https://github.com/webrecorder/warcio) | reading and writing WARC files | Python, Apache 2.0 | 2026-10-17 |
| [iipc/warc2html](https://github.com/iipc/warc2html) | WARC to static HTML, to browse offline or host again | Java, Apache 2.0 | 2025-09-18 |
| [webrecorder/replayweb.page](https://github.com/webrecorder/replayweb.page) | replay of WARC and WACZ files in the browser, on a static host | JavaScript, AGPL 3.0 | 2026-10-22 |
| [webrecorder/pywb](https://github.com/webrecorder/pywb) | an archive replay server | Python, GPL 3.0 | 2026-10-22 |
| [oduwsdl/Reconstructive](https://github.com/oduwsdl/Reconstructive) | a service worker that sends the resources of an archived page to their archived copies | JavaScript, MIT | 2025-03-06 |

Licences as their repositories state them; dates of the last commit on the default branch, read on 24 October 2026.

## 2. Inventory

1. The hosts of the site: every host name and every path it held (Delboy: `perso.club-internet.fr/hdelboy/`, then `herve.delboy.perso.sfr.fr/`).
2. `captures.py <host> --prefix` on each host: every address captured, year by year, in the Wayback Machine, Arquivo.pt and Common Crawl.
3. The author's plan page and the internal links give the scope; the rest of the site goes to a page of its own.

## 3. Missing pages

1. A page whose captures all hold the host's error page: the digest shared by many addresses marks it.
2. `captures.py <address> --plain --sources timemaps,ghost`: the same address in every Memento archive of the directory and in Ghost Archive.
3. `--prefix --name <pattern>`: pages moved inside the site.
4. A web search by theme and by file name: blogs and forums quote the pages, sometimes copy them.
5. archive.today and the portals of the directory, in a browser; the archives on site, by visit or by letter.
6. A page of the site lists the pages to find, with a contact.

## 4. Limits, and the clean ways past them

| limit | clean way |
|---|---|
| rate of an archive | pauses between queries, retries after 429 and 5xx, one year or one crawl per query |
| volume of Common Crawl | its indexes per crawl, then one record by byte range |
| source closed to the assistant | the owner runs the tool from his repository; the assistant reads the result |
| CAPTCHA | a person, in a browser |
| archive on site or restricted | visit, researcher access, letter to the archive |

The procedure keeps to the access each archive grants.

## 5. Publication and checks

As in [recover-a-lost-website.md](recover-a-lost-website.md): pages byte for byte, a reading bar, a table of contents, a search, books printed from the pages, a notice in the manner of a library catalogue, search engines, checks of links, of widths and of the public page, reloaded.

---

# Reconstituer un site depuis les archives du web

La procédure générale, tirée de la remise en ligne du site d'Hervé Delboy.

1. Qui fait quoi : le propriétaire choisit le site, fixe le périmètre et les textes ; l'assistant cherche, code, lit, publie, contrôle, rend compte ; un outil contre une source fermée à l'assistant part d'un bouton de GitHub Actions touché par le propriétaire, ou de l'assistant sur l'ordinateur du propriétaire ; une page derrière un CAPTCHA revient à une personne, dans un navigateur ; une archive sur place (BnF, bibliothèques nationales), à une visite ou une lettre.
2. Lire le code des autres : Reporhogo dans les forges, la liste awesome-web-archiving de l'IIPC ; treize outils de référence, lus et datés (tableau ci-dessus).
3. Inventaire : chaque hôte du site, `captures.py --prefix`, année par année, dans la Wayback Machine, Arquivo.pt et Common Crawl ; la page de plan de l'auteur donne le périmètre.
4. Pages manquantes : l'empreinte partagée repère la page d'erreur de l'hébergeur ; `--plain --sources timemaps,ghost` interroge chaque archive Memento du répertoire ; `--prefix --name` retrouve les pages déplacées ; une recherche sur le web par thème et par nom de fichier ; archive.today et les portails dans un navigateur ; les archives sur place par visite ou par lettre ; une page du site liste les pages à retrouver.
5. Limites et voies propres : pauses et reprises contre le débit ; index par crawl et plage d'octets pour Common Crawl ; l'outil lancé par le propriétaire pour une source fermée à l'assistant ; une personne devant un CAPTCHA ; visite, accès chercheur ou lettre pour une archive restreinte. La procédure suit l'accès que chaque archive accorde.
6. Publication et contrôles : comme pour le site d'Hervé Delboy.

Répertoire des archives : [archives/](../archives/README.md).
