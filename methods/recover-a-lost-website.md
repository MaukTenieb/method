# Recover a lost website

The procedure that put Hervé Delboy's site on alchemy back online in October 2026: 247 pages, two hosts (Club-Internet 1999–2009, SFR 2009–2016), both closed. Result: https://mauktenieb.github.io/alchimie-delboy/ · code: [alchimie-delboy](https://github.com/MaukTenieb/alchimie-delboy). Techniques in detail: [recipes/web-archives.md](../recipes/web-archives.md). French below.

## Who does what

| step | who |
|---|---|
| rules, scope, texts of the site, exceptions | the owner of the project |
| code, reading, checks, publication, report | the assistant |
| a tool run against a source closed to the assistant | the owner, one button in GitHub Actions; or the assistant on the owner's computer |
| reading the results, adding the pages, checking online | the assistant |

## 1. Inventory

1. List every capture of each host: Wayback CDX, `matchType=prefix`, year by year.
2. First pass with `collapse=digest` for the page list; second pass with `collapse` off, every status, for the recovery.
3. Download each page as received: `web.archive.org/web/<ts>id_/<address>`.
4. Decode: ISO-8859-1 declared, cp1252 written.

Code: `scripts/01_inventory.py`, `02_fetch_pages.py`, `common.py`.

## 2. Scope

1. Start from the author's own plan page (`plan_alchimie.htm`): its sections give the core.
2. Follow the internal links; set aside the other domains of the site (astrology, music, chess, statistics, personal pages).
3. Two lists settle the borderline pages: `FORCED_IN`, `FORCED_OUT`.

Code: `scripts/04_classify.py`. Result: 247 pages in, 88 set aside, listed on a page of their own.

## 3. Missing pages

1. A link of the site whose every capture holds the host's error page counts as missing. Club-Internet served that page with the code 200: the digest shared by many addresses and the size band give it away.
2. Recovery, in this order:
   - every capture and every spelling of the address in the Wayback Machine;
   - [Captures](https://github.com/MaukTenieb/reporhogo/tree/main/captures): eight archives, the whole site by prefix, file names by pattern;
   - archive.today in a browser;
   - a web search by theme and by file name: blogs and forums of the 2000s quote the pages and sometimes copy them.
3. A page "Missing pages — to find, help us" lists the rest by file name, with a contact address.

Code: `scripts/09_recover.py`, `14_pages.py`. Result: 46 missing; 6 found, 6 at a new address, 34 to find.

## 4. Publication as the original

1. Each page byte for byte; images and links made local.
2. A reading bar added by two links: plan order, size, font, night, black and white, magnifier, viewer, PDF and EPUB of the page.
3. A table of contents with the facts of each page: revision date, characters, images, capture.
4. A full-text search, sharded by first letters; a result opens the page at the passage.
5. One PDF book per section, printed by Chromium from the pages themselves.

Code: `scripts/13_lecture.py`, `07_build_index.py`, `15_pdf.py`, `site/barre.js`.

## 5. Notice

A record in the manner of a library catalogue, facts only: author, content, original addresses, source, pages set aside, missing pages, interventions. The author's rights line and a contact to hand the site back, in the owner's words.

## 6. Search engines

Title, description, canonical, Open Graph and schema.org for each page, the author's own values kept; `noindex` on redirect stubs and 404; sitemap; `Sitemap:` line in the robots.txt of the domain root; IndexNow; one Search Console property for the domain.

Code: `scripts/16_seo.py`.

## 7. Checks

1. Links, anchors and images of every page (`scripts/08_verify.py`).
2. Playwright on a local server at 390 and 1 280 px: page width, console errors.
3. After each push: the deployment run, then the public page, reloaded.
4. The prose of every page written for the site: [prose/RULES.md](../prose/RULES.md).

---

# Remettre en ligne un site disparu

La procédure qui remet en ligne le site d'Hervé Delboy sur l'alchimie en octobre 2026 : 247 pages, deux hébergeurs fermés (Club-Internet 1999-2009, SFR 2009-2016).

1. Qui fait quoi : le propriétaire du projet fixe les règles, le périmètre, les textes du site et tranche les exceptions ; l'assistant écrit le code, lit, contrôle, publie et rend compte ; un outil à lancer contre une source fermée à l'assistant part d'un bouton de GitHub Actions touché par le propriétaire, ou de l'assistant sur l'ordinateur du propriétaire ; l'assistant lit les résultats, ajoute les pages et vérifie en ligne.
2. Inventaire : toutes les captures de chaque hôte, par préfixe, année par année ; une passe avec `collapse=digest` pour la liste des pages, une passe au complet, dédoublonnage coupé, pour la récupération ; pages téléchargées telles que reçues (`id_`) ; décodage cp1252.
3. Périmètre : la page de plan de l'auteur donne le noyau ; les liens internes l'étendent ; les autres domaines du site passent sur une page à part.
4. Pages manquantes : un lien dont toutes les captures sont la page d'erreur de l'hébergeur ; récupération par toutes les captures et graphies, par [Captures](https://github.com/MaukTenieb/reporhogo/tree/main/captures) (huit archives), par archive.today dans un navigateur, par une recherche sur le web par thème et par nom de fichier ; une page « Pages manquantes — à retrouver, aidez-nous » liste le reste.
5. Publication à l'identique : chaque page à l'octet près, une barre de lecture ajoutée par deux liens, un sommaire en faits, une recherche plein texte, un livre PDF par section imprimé depuis les pages.
6. Notice : une fiche à la manière d'un catalogue de bibliothèque, faits seulement ; la ligne de droits de l'auteur et un contact pour lui rendre le site.
7. Moteurs : balises par page, `noindex` des renvois, sitemap, robots.txt de la racine, IndexNow, Search Console.
8. Contrôles : liens, ancres, images ; Playwright à 390 et 1 280 px ; après chaque envoi, le déploiement puis la page publique rechargée ; la prose selon [prose/RULES.md](../prose/RULES.md).
