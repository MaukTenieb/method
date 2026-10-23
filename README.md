# Method

How Mauk Tenieb builds Insert Koin and the repos around it: hosting, code, Nostr, the watches, images, Tor, the tricks of the trade, the prose rules. For a reader, or for an AI assistant run by a person. French below.

Credit for any reuse: Mauk Tenieb & Korhogo. Code under MIT, this guide under CC BY 4.0, Korhogo material reserved: [LICENSE](LICENSE).

## 1. Principles

1. Every site is a set of flat files on GitHub Pages. Zero server, zero database, zero cost: GitHub budgets are at 0 $ with a hard stop.
2. GitHub workflows do the repeated work (refresh data, rebuild pages, check rules) and commit the result, signed Mauk Tenieb.
3. Each write ends with a check on the public page, reloaded.
4. Before calling a problem unsolvable, [Reporhogo](https://github.com/MaukTenieb/reporhogo) searches 41 code forges for people who solved it, and their code and test data get read.
5. The artist sets the rules and settles the exceptions; the machine types, checks and reports in counts.
6. Facts follow rules and pass through chains; the artist's texts appear as written.

## 2. Insert Koin

Repo [insertkoin](https://github.com/MaukTenieb/insertkoin), site https://mauktenieb.github.io/insertkoin/

- Every file is at the top level (folders: `tor/`, `.github/`, `notes/`, `tools/`), so one upload updates the site.
- `index.html` is the site in English. `fr.html` comes from it: `python3 build-fr.py` after each change.
- `sw.js`, line 2: `const C='ik-YYYYMMDDHHMM'`. A new value at each release makes returning visitors fetch the new code.
- The games load on demand through `kg-loader.js`: `KG.open(name)` fetches `kg-<game>.css`, `.html` and `.js` once, then calls the game's entry point. `KG.onwin(name, detail)` reports each win; the arcade turns it into a Koin.
- Koins: localStorage `ik.koins`, shared with the 3615 (same site, same storage). One Koin opens a game, each win gives one.
- Saved files take a name in the French Republican calendar, then the program, then a counter: `18-vendemiaire-235_photofauna_001.jpg` (`ik-name.js`).

## 3. Nostr

The 3615 and the arcade use the open Nostr network as their only back end. Library: nostr-tools (MIT), served by the site. Relays: relay.damus.io, nos.lol, relay.primal.net, nostr.mom. Each browser keeps one key, `vdx.nostr.sk`, shared by the 3615, the palmarès, the Hall of Kave and Korhogo Kuration.

| Use | Kind | Tag `d` | Content |
|---|---|---|---|
| 3615 presence | 30078 | `3615minitel-presence` | heartbeat every 60 s |
| 3615 directory | 0 | | nickname, for keys made in the 3615 |
| 3615 chat rooms (Kaves) | 42 | | message, proof of work NIP-13, 16 bits |
| 3615 mailbox | 4 | | message, NIP-04, proof of work |
| Palmarès | 30078 | `korhogo-palmares:<game>:<run>` | tags `ini`, `a`, `b` |
| Hall of Kave | 30078 | `korhogo-kave` | the player's card (JSON) |
| Korhogo Kuration | 30078 | `korhogo-kuration` | the visitor's tracks (JSON) |

Kind 30078 is addressable: a relay keeps the last version per key and per `d`. A GitHub workflow of insertkoin reads the relays every hour, checks each signature against `palmares-rules.js` and writes `palmares.json`. Scores stay self-declared: a signature proves the key that sent a score; the rules reject impossible values. Short addresses `mauktenieb.github.io/k/<12 hex>` reach a cassette through the root site's `404.html`.

## 4. Watches

- [Curators](https://github.com/MaukTenieb/curators): every Monday, Claude Code runs on GitHub Actions with a written prompt, reads eight curators' public sources, adds their picks, and two Python programs rank the artists and press VHS cassettes for Insert Koin.
- Public data: the same facts on YouTube, Bandcamp, MusicBrainz, the Internet Archive, Discogs, Wikidata and the sites. Method: [METHOD.md](METHOD.md).
- [Reporhogo](https://github.com/MaukTenieb/reporhogo) searches 41 code forges; [Korhoname](https://github.com/MaukTenieb/Korhoname) checks a name on Discogs, MusicBrainz, trademark registers and known works; [KorhoTube](https://github.com/MaukTenieb/korhotube) lists a channel's videos as JSON. Each one takes a request through a file pushed to `main` (`queue.txt`) and writes the answer to a `result` branch.

## 5. Images

Portraits come as sheets of eight. [Detour](https://github.com/MaukTenieb/detour) cuts a sheet into a sprite strip; Catchlight places the light in the eyes and writes `catchlights.json`. Notes: [Detour](https://mauktenieb.github.io/insertkoin/notes/detour.html), [Catchlight](https://mauktenieb.github.io/insertkoin/notes/catchlight.html).

## 6. Tor in the page

[FaunaTor](https://github.com/MaukTenieb/faunator) runs two Tor clients compiled to WebAssembly (webtor-rs, MIT), over Snowflake. A workflow fetches the Tor consensus twice a day and publishes it on the site, so the page reads it from the same origin.

## 7. Tricks of the trade

- A game closed in a function: a local copy of the page gets a hook (`window.__k = {…}`) before the end of the function; a local server (`python3 -m http.server`) and Playwright drive it. The copy stays out of the repo.
- YouTube offline: a fake `window.YT` records `cueVideoById`, `loadVideoById` and `stopVideo`.
- A calligram (names from widest to narrowest): `canvas.measureText` in the element's computed font, then a sort.
- A platform closed to scripts: a workflow with Playwright in GitHub Actions opens it in a real browser and commits what it reads to a branch.
- A Nostr routine offline: `node --import` with a fake `WebSocket` class.
- Code forges first: before writing a parser or a form filler, read how others do it (NewPipeExtractor test data for YouTube, musicbrainz-userscripts for MusicBrainz forms).

## 8. Prose

Every public text follows six rules: facts (who, what, when, where, why), present tense, active voice, affirmative sentences, plain words, zero slogans. [prose/prose-lint.py](prose/prose-lint.py) flags the patterns of machine-written prose listed by Wikipedia's [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), in English and French, and the house rules. Every Monday, the workflow `prose` runs it on the READMEs and llms.txt files of every MaukTenieb repo and commits the result to [prose/report.md](prose/report.md). Rules in detail: [prose/RULES.md](prose/RULES.md).

```
python3 -I -X utf8 prose/prose-lint.py README.md
```

## 9. Rights and tools

The code of Insert Koin and of these repos comes from an AI assistant, under the direction of the author. Every repo has the same three-part [LICENSE](LICENSE): code under MIT, method under CC BY 4.0, Korhogo material reserved. A person may use an AI assistant to read, explain and adapt the code and the method, with the credit Mauk Tenieb & Korhogo. Training of AI models: reserved, also stated in https://mauktenieb.github.io/.well-known/tdmrep.json and in each site's robots.txt.

---

# Méthode

Comment Mauk Tenieb fabrique Insert Koin et les dépôts qui l'entourent : hébergement, code, Nostr, veilles, images, Tor, tours de main, règles de prose. Pour un lecteur, ou pour un assistant d'IA piloté par une personne.

Mention de toute reprise : Mauk Tenieb & Korhogo. Code sous MIT, ce guide sous CC BY 4.0, matériel Korhogo réservé : [LICENSE](LICENSE).

## 1. Principes

1. Chaque site se compose de fichiers à plat sur GitHub Pages. Zéro serveur, zéro base de données, zéro frais : budgets GitHub à 0 $ avec arrêt.
2. Des workflows GitHub font le travail répété (données, pages, contrôles) et commitent le résultat, signé Mauk Tenieb.
3. Chaque écriture se vérifie sur la page publique, rechargée.
4. Avant de déclarer un problème insoluble, [Reporhogo](https://github.com/MaukTenieb/reporhogo) cherche dans 41 forges de code ceux qui le résolvent ; leur code et leurs données de test passent en lecture.
5. L'artiste fixe les règles et tranche les exceptions ; la machine saisit, contrôle et rend compte en chiffres.
6. Les faits suivent des règles et passent par des chaînes ; les textes de l'artiste paraissent tels qu'il les écrit.

## 2. Insert Koin

- Tous les fichiers à la racine (dossiers : `tor/`, `.github/`, `notes/`, `tools/`) : un envoi met le site à jour.
- `index.html` : le site en anglais ; `fr.html` en découle par `python3 build-fr.py` après chaque modification.
- `sw.js`, ligne 2 : `const C='ik-AAAAMMJJHHMM'` ; une nouvelle valeur à chaque livraison fait charger le nouveau code aux visiteurs.
- Les jeux se chargent à la demande par `kg-loader.js` ; `KG.onwin(nom, détail)` signale chaque victoire, que l'arcade change en Koin.
- Koins : `ik.koins` dans le stockage du navigateur, partagé avec le 3615.
- Fichiers enregistrés : nommés au calendrier républicain, puis le programme, puis un compteur (`ik-name.js`).

## 3. Nostr

Le 3615 et l'arcade se servent du réseau ouvert Nostr comme seul serveur (tableau ci-dessus). Une clé par navigateur, `vdx.nostr.sk`. Un workflow d'insertkoin lit les relais chaque heure, vérifie chaque signature selon `palmares-rules.js` et écrit `palmares.json`. Les scores restent déclaratifs : la signature prouve la clé ; les règles écartent les valeurs impossibles.

## 4. Veilles

- [Curators](https://github.com/MaukTenieb/curators) : chaque lundi, Claude Code tourne dans GitHub Actions avec une consigne écrite, lit les sources de huit curateurs, et deux programmes Python classent les artistes et pressent les cassettes VHS d'Insert Koin.
- Données publiques : mêmes faits sur toutes les plateformes ; méthode : [METHOD.md](METHOD.md).
- Reporhogo, Korhoname, KorhoTube : une demande par fichier poussé sur `main` (`queue.txt`), la réponse sur une branche `result`.

## 5. Images

Planches de huit portraits ; [Detour](https://github.com/MaukTenieb/detour) les découpe en bandes de sprites ; Catchlight place la lumière des yeux.

## 6. Tor dans la page

[FaunaTor](https://github.com/MaukTenieb/faunator) : deux clients Tor en WebAssembly (webtor-rs, MIT) par Snowflake ; consensus Tor publié deux fois par jour sur le site.

## 7. Tours de main

Crochet `window.__k` dans une copie locale pour tester un jeu fermé dans une fonction ; faux `window.YT` pour YouTube hors réseau ; `measureText` pour les calligrammes ; Playwright dans GitHub Actions pour les plateformes fermées aux scripts ; faux `WebSocket` pour une routine Nostr hors réseau ; les forges de code avant tout analyseur ou formulaire.

## 8. Prose

Six règles : faits (qui, quoi, quand, où, pourquoi), présent, voix active, phrases affirmatives, mots simples, zéro slogan. [prose/prose-lint.py](prose/prose-lint.py) relève les tics de la prose de machine (page Signs of AI writing de Wikipédia), en anglais et en français, et les règles maison ; chaque lundi, le workflow `prose` le passe sur les README et llms.txt de tous les dépôts et commite [prose/report.md](prose/report.md).

## 9. Droits et outils

Le code d'Insert Koin et de ces dépôts s'écrit avec un assistant d'IA, sous la direction de l'auteur. Chaque dépôt a la même [LICENSE](LICENSE) en trois parties. Une personne peut se servir d'un assistant d'IA pour lire, expliquer et adapter le code et la méthode, avec la mention Mauk Tenieb & Korhogo. Entraînement de modèles d'IA : réservé.
