# Démarrer ici — écrire sans rouvrir toutes les décisions

**Projet** : roman fantastique à effet documentaire, auteur apparent **Colin Row**; **titre de travail** : *Le Conclave des Sept*.

## En cinq minutes

1. Lire le **canon verrouillé** : `core/00_CANONICAL_STATE.md`.
2. Lire la **forme** : `core/03_VOICE_AND_STYLE.md` et `core/15_GRAMMAIRE_DES_INFLUENCES.md`.
3. Lire le **moteur** : `core/14_STORY_ENGINE.md`.
4. Examiner les **trois intrigues proposées** : `working/STORY_SPINES.md`.
5. Lire une **scène-test** : `material/scene_tests/01_la_norme.md` ou `02_le_refus.md`.

## Pour fabriquer une scène

- Qui est sur le point d'agir? Quel désir humain existait déjà?
- Quel démon a une raison **doctrinale** de vouloir orienter l'issue?
- Quel **ressenti** chez quelle personne est le meilleur levier?
- Quel geste discret change la suite? Pourquoi peut-il aussi s'expliquer sans magie?
- Qui paie, qui bénéficie et quelle conséquence réapparaît plus tard?
- Quel est le **contrefactuel**? Si rien ne change sans l'entité, la scène n'est pas assez forte.

Réduire ensuite la scène à ses pivots; garder le décor seulement s'il détermine l'action. Éviter de conclure par une phrase qui explique ce que le lecteur vient d'observer.

## Où écrire

- **Une idée non approuvée** → `working/` ou `material/`.
- **Un cas contemporain à documenter** → copier `reference/CASE_FILE_TEMPLATE.md` dans `reference/case_files/`.
- **Un chapitre suffisamment décidé pour être rédigé** → `manuscript/part_1/` (ou `part_2/`, `part_3/`), en conservant son statut de brouillon.
- **Une décision explicitement confirmée par l'auteur** → `core/11_CANON_DECISIONS_V1.md` et `core/00_CANONICAL_STATE.md`; ne pas modifier le canon pour faire correspondre un essai à une hypothèse.

## Travail actuel

**Tester trois scènes liées** d'une même intrigue plutôt que rédiger directement dix-huit chapitres. Prendre une première bascule, une conséquence différée et un renversement. Le plan de dix-huit chapitres est un **catalogue provisoire**.

## Construire et contrôler

Depuis la racine du dépôt :

```bash
python3 tools/rebuild.py
python3 tools/check_repo.py
```

Ces scripts utilisent seulement la bibliothèque standard de Python. Le premier recrée les documents de navigation; le second vérifie la cohérence formelle des chemins, du canon et de la compilation.

## Règle de fin

Aucun dévoilement de King Klown dans l'histoire. Après sa toute dernière phrase seulement, un bref remerciement en italique signé King Klown à Réjean McCormick pour ses mains. Voir `core/13_ENDING_PROTOCOL.md`.
