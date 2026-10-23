# Prose rules

The rules of every public text of Mauk Tenieb & Korhogo: READMEs, notes, pages, llms.txt, release notes. `prose-lint.py` flags the places to reread; a person decides. French below.

## Write

1. Facts: who, what, when, where, why. Names, numbers, dates, links.
2. Present tense.
3. Active voice: a person or a program does the action.
4. Affirmative sentences. An absence goes unsaid; a number says « zero » when it counts.
5. Plain words, the way a person writes a note in a workshop.
6. Sentences of varied length.

## Cut

- Slogans, taglines, sales talk, superlatives, puffery.
- Abstract things that act like people: a file that « holds », a page that « carries », a repo that « says », a system that « lives » or « breathes ».
- « X becomes Y » to announce a plan; « not X but Y » and its reverse; « X isn't, Y is ».
- Lists of three for rhythm; colons that stage a reveal; dramatised metaphors for a technical fact.
- Signposts and summaries (« in short », « overall », « at its core », « it's worth noting »).
- Em dashes in a sentence, bold labels in lists, emoji.
- The words of Wikipedia's list of AI vocabulary: crucial, pivotal, robust, seamless, delve, landscape, tapestry, foster, showcase, leverage, and the like.

## Quote

The artist's own texts appear as written, in either language. A translation keeps their tone, their rhythm and their way of naming absence (« Zero X »).

## Check

```
python3 -I -X utf8 prose/prose-lint.py FILE...
```

Every Monday, the workflow `prose` checks the README and llms.txt of every MaukTenieb repo and commits [report.md](report.md).

---

# Règles de prose

1. Des faits : qui, quoi, quand, où, pourquoi ; noms, nombres, dates, liens.
2. Le présent.
3. La voix active : une personne ou un programme fait l'action.
4. Des phrases affirmatives ; une absence se tait ; un nombre dit « zéro » quand il compte.
5. Des mots simples, comme une note d'atelier.
6. Des phrases de longueurs variées.

À retirer : slogans, formules de vente, superlatifs ; choses abstraites qui agissent comme des personnes (un fichier qui « tient », une page qui « porte », un dépôt qui « dit ») ; « X devient Y » pour annoncer un plan ; « ce n'est pas X, c'est Y » ; triades de rythme ; deux-points de révélation ; métaphores dramatisées ; balises et résumés (« en somme », « au fond ») ; tirets cadratins dans la phrase, libellés en gras, emoji ; le vocabulaire de la liste de Wikipédia.

Les textes de l'artiste se citent tels quels ; une traduction garde leur ton et leur manière de nommer l'absence (« Zéro X »).

Credit: Mauk Tenieb & Korhogo. CC BY 4.0 (see [LICENSE](../LICENSE)).
