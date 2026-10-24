# Map of the network

The repos and services of Mauk Tenieb's Korhogo, what each one does, what it reads and what it feeds. French below.

Credit for any reuse: Mauk Tenieb & Korhogo. Rights: [LICENSE](LICENSE).

## Sites

| Repo | Online | Does | Reads | Feeds |
|---|---|---|---|---|
| [mauktenieb.github.io](https://github.com/MaukTenieb/mauktenieb.github.io) | https://mauktenieb.github.io/ | Link page, robots.txt, sitemap.xml and llms.txt of the whole domain; short addresses `/k/<code>` for the Korhogo Kurations | | search and answer engines |
| [insertkoin](https://github.com/MaukTenieb/insertkoin) | https://mauktenieb.github.io/insertkoin/ | The arcade: Korong!, Kompete!, Fauna Chess, Erratik, Faunarratik, Katabatik, the VHS deck, Photofauna, FaunaTor, Skoporhogo, Reporhogo, Kapture, Motel Sound | cassettes of Curators; scores and Kave cards on Nostr; the Tor consensus | palmares.json; the Korhogo Kurations on Nostr; the Tor consensus for FaunaTor |
| [3615](https://github.com/MaukTenieb/3615) | https://mauktenieb.github.io/3615/ | The Minitel: messages, chat, PALMARÈS, Hall of Kave, Kurations, Koins | Nostr relays; palmares.json | Nostr messages with proof of work |
| [katabase](https://github.com/MaukTenieb/katabase) | https://mauktenieb.github.io/katabase | The Korhogo Fauna, aka the Masks: specimens, lore, concept albums | | structured data for engines |
| [curators](https://github.com/MaukTenieb/curators) | https://mauktenieb.github.io/curators/ | Music put forward by eight curators, ranked; VHS cassettes | the curators' public sources, every Monday | `kg-vhs-curations.js` of Insert Koin, row CURATORS |
| [Photofauna](https://github.com/MaukTenieb/Photofauna) | https://mauktenieb.github.io/insertkoin/fotofauna.html | Photo editor: looks stacked on a picture, export in PNG, JPEG, GIF | | Insert Koin |

## Tools

| Repo | Does | Request | Answer |
|---|---|---|---|
| [reporhogo](https://github.com/MaukTenieb/reporhogo) | Searches 41 code forges for a topic | `queue.txt` on `main` | branch `result` |
| [reporhogo/captures](https://github.com/MaukTenieb/reporhogo/tree/main/captures) | Captures: lists every capture of an address or a site in 17 web archives, downloads the readable ones | `captures/queue.txt`, `captures/archives.json`; run by hand | branch `archives` |
| [Korhoname](https://github.com/MaukTenieb/Korhoname) | Checks a name on Discogs, MusicBrainz, Wikidata, Wikipedia, TMview, INPI | `queue.txt` on `main` | branch `result` |
| [korhotube](https://github.com/MaukTenieb/korhotube) | Lists a YouTube channel's videos as JSON | `queue.txt` on `main` | branch `result` |
| [detour](https://github.com/MaukTenieb/detour) | Cuts a sheet of eight portraits into a sprite strip | a sheet | the sprites of Korong! and Faunarratik |
| [faunator](https://github.com/MaukTenieb/faunator) | Two Tor clients in a web page, over Snowflake | the consensus published by Insert Koin | FaunaTor in Insert Koin |
| [torview](https://github.com/MaukTenieb/torview) | A desktop web browser in Go through the official Tor daemon | | |
| [method](https://github.com/MaukTenieb/method) | This guide; prose rules and prose-lint; the weekly coherence check | every public repo | `prose/report.md`, `coherence/report.md` |
| [MaukTenieb](https://github.com/MaukTenieb/MaukTenieb) | The GitHub profile page | | |

Insert Koin replaces the former site, `korhogo`, an archived repo.

## The week

| When (UTC) | Who | What |
|---|---|---|
| every hour | workflow of insertkoin | palmares.json from the Nostr scores |
| twice a day | workflow of insertkoin | the Tor consensus under `tor/` |
| Sunday night | Claude routine | the private workshop log of decisions and work brought up to date |
| Monday 6:23 | workflow `coherence` of method | rights, retired names, Medium links, prose, dead links, repo by repo |
| Monday 7:37 | workflow `prose` of method | prose-lint on every README and llms.txt |
| Monday morning | Claude routines | Curators cassettes; corrections after the two reports; rewrites put to the author |

The author sets the rules and settles the exceptions. The routines correct facts and links, and put every rewrite of a text to the author before it goes online.

---

# Carte du réseau

Les dépôts et services de Korhogo, de Mauk Tenieb : ce que fait chacun, ce qu'il lit, ce qu'il alimente. Les tableaux ci-dessus valent pour les deux langues ; voici leur lecture en français.

- Sites : mauktenieb.github.io (page de liens, robots.txt, sitemap.xml, llms.txt, adresses courtes `/k/<code>`) ; Insert Koin (la salle de jeux) ; 3615 (le Minitel) ; Katabase (la Korhogo Fauna, aka the Masks) ; Curators (la musique de huit curateurs, les cassettes VHS de la rangée CURATORS) ; Photofauna (l'éditeur de photos).
- Captures, outil de Reporhogo, cherche une page perdue dans 17 archives du web ; lancé à la main, il répond sur la branche `archives`.
- Outils : Reporhogo, Korhoname, KorhoTube reçoivent une demande par `queue.txt` sur `main` et répondent sur la branche `result` ; Detour découpe les planches de portraits ; FaunaTor et TorView passent par Tor ; method contient ce guide, les règles de prose et le contrôle de cohérence ; MaukTenieb est la page de profil. Insert Koin remplace l'ancien site, `korhogo`, un dépôt archivé.
- La semaine : palmarès chaque heure ; consensus Tor deux fois par jour ; dimanche soir, le journal privé des décisions et du travail ; lundi 6 h 23 UTC, le contrôle de cohérence ; 7 h 37 UTC, le contrôle de prose ; lundi matin, les cassettes de Curators, les corrections, les réécritures soumises à l'auteur.

L'auteur fixe les règles et tranche les exceptions. Les routines corrigent les faits et les liens, et soumettent à l'auteur chaque réécriture d'un texte avant sa mise en ligne.
