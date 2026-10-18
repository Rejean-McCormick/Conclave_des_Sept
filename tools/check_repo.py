#!/usr/bin/env python3
"""Lightweight repository quality checks; no third-party dependencies."""
from __future__ import annotations
from pathlib import Path
import re, sys
ROOT=Path(__file__).resolve().parents[1]
errors=[]
files=[p for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in p.parts]
contents={p:p.read_text(encoding='utf8') for p in files if p.suffix=='.md'}

# Local Markdown targets only; explicitly ignore http/mailto/fragment and sandbox URLs.
linkpat=re.compile(r'(?<!!)\[[^\]]*\]\(([^)]+)\)')
for p, s in contents.items():
    for match in linkpat.finditer(s):
        target=match.group(1).split('#',1)[0].strip()
        if not target or re.match(r'^(https?://|mailto:|sandbox:)',target): continue
        if not (p.parent/target).exists(): errors.append(f'Broken local link: {p.relative_to(ROOT)} -> {target}')

# Mandatory files and scope guardrails
must=['core/00_CANONICAL_STATE.md','core/13_ENDING_PROTOCOL.md','core/15_GRAMMAIRE_DES_INFLUENCES.md','working/STORY_SPINES.md','reference/CASE_FILE_TEMPLATE.md','tools/rebuild.py']
for r in must:
    if not (ROOT/r).exists(): errors.append('Missing: '+r)

manuscripts=list((ROOT/'manuscript').rglob('*.md'))
for p in manuscripts:
    if p.name=='README.md': continue
    if re.search(r'king klown|réjean mccormick',p.read_text(encoding='utf8'),re.I):
        errors.append('Possible King Klown/Réjean reveal in manuscript: '+str(p.relative_to(ROOT)))

if len(list((ROOT/'chapter_briefs').glob('*.md')))!=18:
    errors.append('Expected 18 PROPOSED briefs (update test if structure is explicitly revised)')

# Deterministic outputs consistency without deleting/re-writing on failed runs
for doc in ['INDEX.md','REPO_MANIFEST.md','FULL_CONTENT.md']:
    if not (ROOT/doc).exists(): errors.append('Missing generated '+doc)

s=(ROOT/'core/00_CANONICAL_STATE.md').read_text(encoding='utf8')
for term in ['Lucifer','démons','King Klown','Colin Row']:
    if term not in s: errors.append('Canonical summary missing term '+term)

if errors:
    print('Repository validation FAILED:')
    for e in errors: print(' -',e)
    sys.exit(1)
print(f'OK — {len(files)} files, {len(contents)} Markdown documents; links and core guardrails checked.')
