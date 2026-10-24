# Platforms

YouTube, Bandcamp, MusicBrainz, the Internet Archive, Discogs, trademark registers: reading and writing the same facts everywhere. Method: [METHOD.md](../METHOD.md). French summary in [README.md](README.md).

## YouTube

### Exact descriptions, real links

Obstacle. Read from the page, a description holds shortened link labels, and the offsets drift after an emoji.

Technique. Take `attributedDescription` from the youtubei `next` answer. Encode the text in UTF-16-LE and cut at `2 × startIndex`: YouTube counts in UTF-16 units. Each `commandRun` becomes its `urlEndpoint` (unwrap `youtube.com/redirect?q=`), its `watchEndpoint` (keep `&t=`) or its `browseEndpoint`.

Code. Private repository of the chain.

### From a server, `next` answers

Obstacle. From runners and Workers, every InnerTube player client meets "Sign in to confirm you're not a bot".

Technique. POST `youtubei/v1/next` for title, description, date, views and chapters; player data from the watch page on a home connection only (flag `playerBlocked`). Headers `CONSENT=YES+1; SOCS=CAI`; embedded JSON taken out by brace counting; for each field, the source that answered.

Code. [korhotube/korhotube.mjs](https://github.com/MaukTenieb/korhotube/blob/main/korhotube.mjs).

### Every video of a channel, keyless

Obstacle. RSS gives 15 videos.

Technique. Browse `VLUU` + `channelId[2:]`, the uploads playlist, and follow the `continuationCommand` tokens, up to 200 pages. Duration: the badge of `lockupViewModel.contentImage`. One video id checks fast against `youtube.com/oembed`.

Code. [korhotube/korhotube.mjs](https://github.com/MaukTenieb/korhotube/blob/main/korhotube.mjs).

### Writing from Actions with the owner's consent

Obstacle. A headless runner opens zero browser consent page.

Technique. An OAuth client of type "TVs and Limited Input devices" and `oauth2.googleapis.com/device/code`: the run prints a code, the owner types it at https://www.google.com/device. The refresh token returns as a repository secret, sealed with the repository's public key (PyNaCl `SealedBox`); later runs skip the code.

### Bulk writes within the quota

Obstacle. `videos.update` costs 50 of 10 000 daily units.

Technique. Compare the live text with the target before each write; save `before.json` after each successful write; stop on `quotaExceeded` (reset at midnight, Pacific time); restore from the backup of the previous run.

### Link chips

Obstacle. YouTube turns Facebook, X and channel links of a description into logo chips, whatever the spelling.

Technique. A redirect page on one's own domain (`/facebook`) keeps a plain address. Source: the test mocks of NewPipeExtractor and its `YoutubeDescriptionHelper`.

## Bandcamp

### Pages served to bots, `data-tralbum` absent

Obstacle. Runners receive a page variant with zero album JSON.

Technique. Fall back to `ld+json` (`description`, `creditText`), then to `div.tralbumData` (about, credits) and `div#license`. `<br>` marks the line breaks of the text; raw newlines belong to the layout.

## MusicBrainz

### The release editor filled from a page

Obstacle. Dozens of releases to type, and zero write API.

Technique. A hidden `<form method="post" action="https://musicbrainz.org/release/add" target="_blank">` with the field names of murdos/musicbrainz-userscripts and derat/yambs (`artist_credit.names.N.*`, `mediums.0.track.N.*`, `urls.N.link_type`, `edit_note`). Artists: GET `/artist/create?edit-artist.*`. Genres go as tags afterwards. A new artist reaches the search a few minutes later.

Code. [mauktenieb.github.io/mb/index.html](https://github.com/MaukTenieb/mauktenieb.github.io/blob/main/mb/index.html).

### Complete reads

Obstacle. Reads stopped at 100 release groups; answers 503 left gaps.

Technique. 1.1 s between calls; `offset` up to `release-group-count`; six retries on 503 with growing waits; unread entries marked as such. Official genres: `ws/2/genre/all?fmt=txt`.

## Internet Archive

### Metadata rewritten with a way back

Technique. POST `archive.org/metadata/<id>` with `-target=metadata` and `-patch` (JSON Patch), header `Authorization: LOW access:secret`, 1.5 s apart. Old values go to a backup branch. Links compare after URL decoding: percent encoding alone caused a rewrite at every run.

## Names

### A name against Discogs, MusicBrainz and the registers

Technique. Discogs: monthly dumps through `data.discogs.com/?prefix=data/YYYY/`, read with `ElementTree.iterparse` (found in ofurkancoban/DiscogsCLI). TMview: POST `tmdn.org/tmview/api/search/results` with `{page, pageSize, criteria: 'C', basicSearch}`; marks in force in classes 9 and 41 count. Names compare on one form: NFKD fold, punctuation out, θ þ ð ß ø đ ł transliterated. Each source returns a verdict, "unreadable" included.

Code. [Korhoname/korhoname.py](https://github.com/MaukTenieb/Korhoname/blob/main/korhoname.py).
