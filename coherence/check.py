#!/usr/bin/env python3
"""Weekly check of every public repository of MaukTenieb on GitHub.
Reads each repository (shallow clone) and reports, file by file:
  rights    - a LICENSE with "Mauk Tenieb" and "Korhogo"; a README with a rights line in their name
  names     - forms retired by the names policy (noms.json of the private atelier): "Naphta/Naphta-Kerema",
              "Inn Eskort", "Puck You", "Motel Puck" in visible texts
  medium    - links to the Medium account (kept, out of the public listings since 23 Oct 2026)
  prose     - stock patterns of machine-written prose in READMEs and notes (prose/prose-lint.py)
  links     - external links of the READMEs that answer with an error
Writes report.md and report.json in the current folder. Copyright (c) 2026 Mauk Tenieb & Korhogo, MIT licence (see LICENSE).
"""
import json, os, re, subprocess, sys, time, urllib.request, urllib.error
OWNER = 'MaukTenieb'
UA = {'User-Agent': 'method-coherence (Mauk Tenieb & Korhogo)'}
TOKEN = os.environ.get('GITHUB_TOKEN', '')
TEXT = re.compile(r'\.(md|html?|txt|json|js|py|yml|yaml)$', re.I)
SKIP = re.compile(r'(^|/)(node_modules|\.git|vendor)/|nostr-tools\.js$|\.min\.js$|kg-vhs-curations\.js$|catalogue\.json$|palmares\.json$|(^|/)report\.md$|prose/RULES\.md$')
RETIRED = [('Naphta/Naphta-Kerema', 'Naphta-Kerema seul dans les présentations formelles, Naphta ailleurs'),
           ('Inn Eskort', 'retiré de l\'enseigne le 23 oct. 2026'), ('INN ESKORT', 'retiré de l\'enseigne le 23 oct. 2026'),
           ('Puck You', 'ancien nom de Korong!'), ('Motel Puck', 'ancien nom de Korong!')]
MEDIUM = re.compile(r'(mauktenieb\.medium\.com|medium\.com/@mauktenieb)', re.I)
LINK = re.compile(r'https?://[^\s)<>"\'`\]]+')

def api(path):
    h = dict(UA)
    if TOKEN: h['Authorization'] = 'Bearer ' + TOKEN
    with urllib.request.urlopen(urllib.request.Request('https://api.github.com' + path, headers=h), timeout=60) as r:
        return json.load(r)

def repos():
    if os.environ.get('REPOS'):  # a fixed list, for a run outside GitHub Actions
        return [{'name': n, 'clone_url': 'https://github.com/%s/%s' % (OWNER, n)} for n in os.environ['REPOS'].split()]
    out, page = [], 1
    while True:
        a = api('/users/%s/repos?type=owner&per_page=100&page=%d' % (OWNER, page))
        out += [r for r in a if not r.get('private') and not r.get('fork')]
        if len(a) < 100: return out
        page += 1

def alive(url):
    for m in ('HEAD', 'GET'):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, method=m, headers=UA), timeout=20) as r: return r.status
        except urllib.error.HTTPError as e:
            if m == 'GET' or e.code not in (403, 405): return e.code
        except Exception as e:
            if m == 'GET': return 'error'
    return 'error'

def main(work):
    lint = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'prose', 'prose-lint.py')
    R = {'checked': time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime()), 'repos': {}}
    for r in repos():
        name = r['name']; d = os.path.join(work, name)
        subprocess.run(['git', 'clone', '-q', '--depth', '1', r['clone_url'], d], check=False)
        rep = {'archived': r.get('archived', False), 'rights': [], 'names': [], 'medium': [], 'prose': [], 'links': []}
        lic = os.path.join(d, 'LICENSE')
        lt = open(lic, encoding='utf-8', errors='replace').read() if os.path.exists(lic) else ''
        if not ('Mauk Tenieb' in lt and 'Korhogo' in lt): rep['rights'].append('LICENSE sans « Mauk Tenieb » et « Korhogo »' if lt else 'LICENSE absent')
        rd = next((os.path.join(d, f) for f in ('README.md', 'readme.md', 'README') if os.path.exists(os.path.join(d, f))), None)
        rt = open(rd, encoding='utf-8', errors='replace').read() if rd else ''
        if not rd: rep['rights'].append('README absent')
        elif not re.search(r'(©|\(c\)|Copyright|Credit for any reuse|Cr[ée]dit)[^\n]*(Mauk Tenieb|Korhogo)', rt, re.I): rep['rights'].append('README sans ligne de droits au nom de Mauk Tenieb & Korhogo')
        for root, _, files in os.walk(d):
            for f in files:
                p = os.path.join(root, f); rel = os.path.relpath(p, d)
                if not TEXT.search(f) or SKIP.search(rel): continue
                try: t = open(p, encoding='utf-8', errors='replace').read()
                except Exception: continue
                for w, why in RETIRED:
                    n = t.count(w)
                    if n: rep['names'].append('%s : « %s » ×%d (%s)' % (rel, w, n, why))
                if MEDIUM.search(t): rep['medium'].append(rel)
                if f.lower().endswith('.md') and not rel.startswith('.github'):
                    res = subprocess.run([sys.executable, lint, p], capture_output=True, text=True)
                    hits = [l for l in res.stdout.splitlines() if l.strip() and not l.startswith(' ')]
                    if hits: rep['prose'].append('%s : %d passages à relire' % (rel, len(hits)))
        for u in sorted(set(LINK.findall(rt)))[:60]:
            u = u.rstrip('.,;:')
            s = alive(u)
            if s == 'error' or (isinstance(s, int) and s >= 400 and s not in (403, 429)): rep['links'].append('%s → %s' % (u, s))
        R['repos'][name] = rep
        print(name, {k: len(v) for k, v in rep.items() if isinstance(v, list)}, file=sys.stderr)
    json.dump(R, open('report.json', 'w'), ensure_ascii=False, indent=1)
    with open('report.md', 'w', encoding='utf-8') as f:
        f.write('# Coherence — %s\n\nPublic repositories of %s, checked one by one.\n' % (R['checked'], OWNER))
        for name, rep in sorted(R['repos'].items()):
            f.write('\n## %s%s\n\n' % (name, ' (archived)' if rep['archived'] else ''))
            any_ = False
            for k, title in (('rights', 'Rights'), ('names', 'Names'), ('medium', 'Medium links'), ('prose', 'Prose to reread'), ('links', 'Dead links')):
                if rep[k]:
                    any_ = True; f.write('%s:\n' % title)
                    for x in rep[k]: f.write('- %s\n' % x)
            if not any_: f.write('Clean.\n')
        f.write('\nCopyright © Mauk Tenieb & Korhogo.\n')

if __name__ == '__main__':
    os.makedirs(sys.argv[1], exist_ok=True); main(sys.argv[1])
