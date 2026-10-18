#!/usr/bin/env python3
"""Rebuild navigational files in a portable Markdown writing repository.

Only Python standard library; source texts are indexed but NOT replicated in
FULL_CONTENT because those are supplied as separate, original source files.
"""
from __future__ import annotations
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
EXCLUDE_NAMES={'FULL_CONTENT.md','INDEX.md','REPO_MANIFEST.md'}
SECTIONS=[
 ('Démarrage', ['START_HERE.md','README.md','STATUS_MATRIX.md','working/CHANGELOG.md']),
 ('Noyau de production', sorted(str(p.relative_to(ROOT)) for p in (ROOT/'core').glob('*.md'))),
 ('Parties proposées', sorted(str(p.relative_to(ROOT)) for p in (ROOT/'parts').glob('*.md'))),
 ('Fiches de chapitre proposées', sorted(str(p.relative_to(ROOT)) for p in (ROOT/'chapter_briefs').glob('*.md'))),
 ('Documentation et sources', sorted(str(p.relative_to(ROOT)) for p in (ROOT/'reference').glob('*.md')) + ['reference/case_files/README.md','reference/sources/Determinisme_divin_v14.md','reference/sources/The_Human_Being_as_a_Prompted_Creature_2026.txt']),
 ('Atelier et intrigues', sorted(str(p.relative_to(ROOT)) for p in (ROOT/'working').rglob('*.md'))),
 ('Matériaux', sorted(str(p.relative_to(ROOT)) for p in (ROOT/'material').rglob('*.md'))),
 ('Manuscrit', sorted(str(p.relative_to(ROOT)) for p in (ROOT/'manuscript').rglob('*.md'))),
 ('Outillage', ['tools/rebuild.py','tools/check_repo.py']),
]

def main():
    index=['# Index du dépôt — version v2','', '**Priorité de lecture :** [`START_HERE.md`](START_HERE.md) puis [`core/00_CANONICAL_STATE.md`](core/00_CANONICAL_STATE.md).', '', 'Les noms de chapitres, le nombre d’entités et les intrigues restent des **propositions**.', '']
    for title, paths in SECTIONS:
        index += [f'## {title}', '']
        for path in paths:
            if not (ROOT/path).exists(): raise FileNotFoundError(path)
            index.append(f'- [`{path}`]({path})')
        index.append('')
    (ROOT/'INDEX.md').write_text('\n'.join(index).rstrip()+'\n',encoding='utf8')

    paths=sorted(p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file() and p.name!='.DS_Store' and '__pycache__' not in p.parts)
    manifest=['# Manifeste du dépôt — v2','', 'Fichiers présents, chemins relatifs à la racine; liste régénérable avec `python3 tools/rebuild.py`.', '']
    manifest.extend('- `'+p+'`' for p in paths)
    (ROOT/'REPO_MANIFEST.md').write_text('\n'.join(manifest)+'\n',encoding='utf8')

    contents=['# Compilation de travail — v2','','> Document **généré** par `python3 tools/rebuild.py`. Modifier les fichiers individuels, jamais cette compilation. Les textes-source intégraux sont conservés séparément sous `reference/sources/`. Les scripts et les binaires ne sont pas compilés.','']
    for title, paths in SECTIONS:
        compiled=[p for p in paths if p.endswith('.md') and not p.startswith('reference/sources/')]
        if not compiled: continue
        contents.extend([f'# {title}', ''])
        for path in compiled:
            if path in EXCLUDE_NAMES: continue
            contents += [f'## Fichier : `{path}`', '', (ROOT/path).read_text(encoding='utf8').rstrip(), '', '---', '']
    (ROOT/'FULL_CONTENT.md').write_text('\n'.join(contents).rstrip()+'\n',encoding='utf8')
    print('Generated INDEX.md, REPO_MANIFEST.md, FULL_CONTENT.md')

if __name__=='__main__': main()
