# Compilation de travail — v2

> Document **généré** par `python3 tools/rebuild.py`. Modifier les fichiers individuels, jamais cette compilation. Les textes-source intégraux sont conservés séparément sous `reference/sources/`. Les scripts et les binaires ne sont pas compilés.

# Démarrage

## Fichier : `START_HERE.md`

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

---

## Fichier : `README.md`

# Le Conclave des Sept — dépôt d’écriture et de recherche v2

**Titre de travail uniquement.** Roman philosophique et fantastique à réalisme documentaire, signé **Colin Row**.

## Proposition

Des démons, protagonistes du récit, cherchent à préparer une manifestation de Dieu par la rupture des ordres humains. Les anges poursuivent le même horizon par la cohésion et la stabilité. Tous agissent surtout en infléchissant **des émotions et les chaînes de circonstances** : la personne influencée agit et reconstruit ensuite une explication qu'elle croit personnelle. La guerre céleste remonte à la chute de Lucifer et d'une moitié des anges, selon **la cosmologie de cette fiction**, non comme assertion sur la tradition religieuse.

L'enjeu n'est pas « qui a raison politiquement? », mais : **à qui appartient un choix lorsqu'une impulsion qui semble venir de soi a été préparée ailleurs?**

## Voix recherchée

Prose **condensée, causale, sensible** : peu de décor, peu d'attente, plusieurs lectures possibles dans une même scène. Le lecteur doit penser « on dirait presque que cela se passe ainsi », sans que le livre prétende apporter la preuve d'interventions surnaturelles réelles. Anges et démons se parlent entre eux; aux humains, ils transmettent des ressentis et des impulsions, **pas des phrases télépathiques**.

## Statuts

- **CANON** : fixé explicitement par l'auteur en conversation.
- **PROPOSITION** : choix de travail pour écrire et tester; modifiable sans retcon.
- **RÉSERVE** : option ouverte, non autorisée à devenir un fait tacite.
- **SOURCE** : texte ou idée préexistante, qui n'est pas automatiquement canon.

## Architecture inspirée du dépôt de référence `Colin_Row.zip`

- `core/` : canon, bible, personnages, style, causalité, règles d'influence, fins et protocole d'écriture.
- `parts/` : progression dramatique **proposée** en trois mouvements.
- `chapter_briefs/` : dix-huit **hypothèses** de chapitres, non un plan approuvé.
- `reference/` : sources de l'auteur, vérification factuelle et garde-fous relatifs aux personnes réelles.
- `material/` : fragments / essais non canoniques / scènes / options écartées.
- `manuscript/` : futur roman, séparé de la documentation.
- `working/` : expérimentation, décisions en attente.
- `FULL_CONTENT.md` : compilation **générée** des documents de production, hors sources intégrales.
- `START_HERE.md` et `STATUS_MATRIX.md` : parcours rapide et statuts des décisions.
- `tools/` : scripts autonomes de régénération et vérification.

## Ordre de lecture pour écrire

0. `START_HERE.md` : démarrage, choix et procédures
1. `core/00_CANONICAL_STATE.md`
2. `core/03_VOICE_AND_STYLE.md`
3. `core/12_INFLUENCE_MECHANICS.md`
4. `core/09_CHAINES_DE_CAUSALITE.md`
5. brief concerné dans `chapter_briefs/`
6. `core/06_CONTINUITY_MAP.md`
7. sources factuelles pertinentes dans `reference/`

## Restrictions créatives essentielles

- Pas d'explication de l'univers **King Klown** dans ce livre.
- **Colin Row** est le pseudonyme de publication. **Réjean McCormick** n'est pas présenté au lecteur pendant le récit.
- Après la dernière ligne du roman, un bref remerciement **en italique, attribué à King Klown**, constitue l'unique point de connexion explicite.
- La documentation peut tout savoir; la prose n'a pas à tout expliquer.
- `Colin_Row.zip` sert de modèle d'**organisation de travail**, non de réservoir narratif à fusionner avec ce livre.

## Ce que la v2 améliore

- `core/14_STORY_ENGINE.md` : donne une vraie nécessité de passer d’un chapitre au suivant.
- `core/15_GRAMMAIRE_DES_INFLUENCES.md` : précise la perturbation émotionnelle, les relais et le test contrefactuel.
- `core/16_DOCTRINES_EN_CONFLIT.md` : différencie les démons comme protagonistes, sans changement de camp.
- `core/17_COURBE_DU_LECTEUR.md` : suit la progression de l’ébahissement vers la paix.
- `working/STORY_SPINES.md` : trois options **non décidées** pour l’intrigue.
- `working/RECURRING_HUMAN_THREADS.md` : vies récurrentes fictives, **non décidées**.
- `material/scene_tests/` : cinq scènes d'essai **non canoniques**, brèves et causales.
- `reference/CASE_STUDY_PROTOCOL.md` : protocoles de recherche sur personnages réels.
- `tools/` : génération reproductible de la navigation et vérification des fichiers.

## Prochaine étape

Tester trois scènes **enchaînées**, chacune avec une bascule et un effet différé. Les 18 briefs sont des hypothèses thématiques, **pas** un sommaire définitif. Garder le canon et les propositions séparés.

Pour régénérer l'index, le manifeste et la compilation : `python3 tools/rebuild.py`. Pour valider la structure : `python3 tools/check_repo.py`.

---

## Fichier : `STATUS_MATRIX.md`

# Matrice de statut — ce qui est sûr et ce qui ne l'est pas

| Sujet | Statut | Autorité | Fichier |
|---|---|---|---|
| Protagonistes démoniaques | **CANON** | réponse explicite de l'auteur | `core/00_CANONICAL_STATE.md` |
| Chute de Lucifer avec moitié des anges; aucune conversion | **CANON de fiction** | réponse explicite | `core/00_CANONICAL_STATE.md` |
| Influence par émotion, intuition, lapsus, guidage bref | **CANON qualitatif** | réponses explicites | `core/12_INFLUENCE_MECHANICS.md` |
| Réseau de relais humains; l'appel est aussi orienté | **CANON** | correction explicite de l'auteur | `core/15_GRAMMAIRE_DES_INFLUENCES.md` |
| Narration condensée, ressenti, doubles lectures | **CANON** | correction explicite | `core/03_VOICE_AND_STYLE.md` |
| Livre fictionnel, quasi documentaire, réalité extrapolée | **CANON** | réponse explicite | `core/02_EDITORIAL_CONTRACT.md` |
| Signature finale King Klown / Réjean, aucune explication | **CANON** | réponse explicite | `core/13_ENDING_PROTOCOL.md` |
| Titre *Le Conclave des Sept* | **PROPOSITION** | convention de travail | `README.md` |
| 7 anges + 7 démons nommés | **PROPOSITION** | esquisse ancienne | `core/04_CHARACTER_BIBLE.md` |
| Trois actes / 18 chapitres | **PROPOSITION** | échafaudage | `core/10_CHAPTER_ENGINE.md` |
| Rupture protagoniste principal | **PROPOSITION** | hypothèse dramatique | `working/STORY_SPINES.md` |
| Nora, Malik, Élise, Victor | **PROPOSITION** | fils humains proposés | `working/RECURRING_HUMAN_THREADS.md` |
| Nature de la manifestation divine | **OUVERT** | aucune décision | `core/07_AMBIGUITIES_AND_DECISIONS.md` |
| Identité des personnages publics et événements | **OUVERT / DOCUMENTATION NÉCESSAIRE** | recherches à faire | `reference/REAL_PEOPLE_AND_HISTORY.md` |
| Textes philosophiques de 2015 et 2026 | **SOURCE** | œuvres antérieures de l'auteur | `reference/SOURCE_INDEX.md` |

**Principe :** un document exploratoire ne crée pas du canon par répétition. L'utilisateur peut changer les propositions sans retoucher les invariants du monde.

---

## Fichier : `working/CHANGELOG.md`

# Historique des révisions

## v2 — enrichissement éditorial et outillage

- **Conservé** : la totalité du dépôt v1, ses 18 briefs exploratoires et les deux textes-source de l'auteur.
- **Clarifié** : différence entre canon explicite, outil éditorial, proposition d'intrigue et document source.
- **Ajouté** : moteur dramatique, grammaire des influences, contradictions doctrinales, continuité causale, courbe de lecture.
- **Ajouté** : pistes d'intrigue, fils humains récurrents proposés, scènes-tests brèves, fiches de recherche, scorecard, guide de démarrage.
- **Enrichi** : briefs pour distinguer les séquences et préparer les effets différés.
- **Automatisé** : génération de `FULL_CONTENT.md`, `INDEX.md`, `REPO_MANIFEST.md` et validation structurelle.
- **Non décidé** : titre, nombre de chapitres, figure principale, apparition de Dieu et sélection de personnalités réelles.

Aucun texte du manuscrit n'a été déclaré final. Aucun cas historique controversé n'a été fact-checké dans cette livraison.

---

# Noyau de production

## Fichier : `core/00_CANONICAL_STATE.md`

# État canonique — v1 (18 octobre 2026)

## Ce que l'auteur a fixé

1. **Univers** : l'histoire se déroule dans notre monde, nourrie d'événements réels **extrapolés en fiction**. Réalité sociale reconnaissable; couche céleste inventée.
2. **Séparation** : depuis la chute de Lucifer avec **la moitié des anges**, anges et démons constituent deux camps distincts; **aucun changement de camp**.
3. **Point de vue** : les **démons** sont les protagonistes. Les anges sont aussi essentiels à la confrontation, mais ne prennent pas le centre du récit.
4. **Missions** : les démons voient la fragmentation/rupture comme la condition du renouveau et de la manifestation divine; les anges recherchent la cohérence/structure pour une manifestation divine. Les deux systèmes peuvent produire du bien et du mal vus de l'humain.
5. **Influence** : tous les humains peuvent être orientés à des degrés variables; la prise dépend du contexte, de la réceptivité, de ce qui résonne déjà en eux.
6. **Canal** : les entités influencent par **émotions, intuitions, attirance, répulsion, impulsions**, parfois lapsus, trous de mémoire et contrôle moteur passager lors de fragilité émotionnelle. **Pas de phrases envoyées comme dialogues intérieurs.**
7. **Causalité à plusieurs personnes** : susciter un appel chez A, l'acheminer via B et modifier la décision de C est parfois préférable à toucher directement C.
8. **Personnalités célestes** : êtres philosophiques, rigides, absolus, définis par leurs missions. Ils ne sont pas psychologiquement de simples humains aux ailes visibles.
9. **Écriture** : extrême densité; pas de décors décoratifs ni de scènes d'attente; primauté des ressentis et de la causalité; possibilité de **deux histoires superposées** (explication ordinaire / stratégie céleste).
10. **Promesse au lecteur** : crédibilité « presque documentaire »; étonnement final, puis paix devant une responsabilité humaine moins souveraine qu'il n'y paraît. Le roman explore le déterminisme divin comme **hypothèse fictionnelle**, non comme démonstration scientifique.
11. **Signature** : auteur publié sous **Colin Row**; univers King Klown **non dévoilé** dans le récit; dernier paragraphe en italique signé King Klown remerciant Réjean de lui avoir prêté ses mains. Aucun commentaire explicatif après.

## Ne pas traiter comme acquis

- Le **titre** (*Le Conclave des Sept*) et le **nombre de 7** entités nommées de chaque côté sont des propositions de travail.
- Les noms et traits détaillés des entités restent ajustables; voir `04_CHARACTER_BIBLE.md`.
- La réalité objective d'une **manifestation finale de Dieu**, sa forme, sa chronologie et l'interprétation exacte du mandat céleste sont **ouvertes**.
- La liste des dirigeants humains, le nombre de chapitres et les scènes historiques ne sont **pas approuvés**.
- L'idée que les entités connaissent l'avenir, ont un rang hiérarchique stable, ou payent un prix physique pour l'influence n'est **pas décidée**.

## Conflit moteur

**L'ordre veut protéger les vies en les encadrant. La rupture veut libérer les possibilités en démantelant les cadres. Chacun peut sauver dans un cas et détruire dans un autre.** Les êtres célestes voient surtout leurs fins; les humains vivent les conséquences.

## Important : responsabilité

L'existence d'une influence dans le **roman** n'excuse pas mécaniquement les actes ni ne constitue une affirmation sur les causes réelles d'un crime ou d'une décision politique. Le texte peut questionner la culpabilité morale sans confondre ce questionnement avec l'absence de conséquences ou de recours pour les victimes.

---

## Fichier : `core/01_BOOK_BIBLE.md`

# Bible du livre — v1

## Logline (proposition)

Depuis la chute de Lucifer, les démons tentent de desserrer les systèmes humains pour rendre possible une incarnation divine. Les anges, persuadés du contraire, stabilisent les institutions. Leur lutte n'est ni publique ni miraculeuse : une émotion au bon moment, un appel suscité chez une autre personne, une seconde de colère suffisent parfois à infléchir une destinée politique, économique ou intime.

## Sujet apparent

Le conflit d'êtres célestes autour du pouvoir, de l'économie et des décisions humaines — décisions réelles servant d'appuis à une histoire fictive.

## Sujet profond

**L'humain se pense auteur de ses décisions alors qu'il répond souvent à des sollicitations qu'il n'a ni conçues ni remarquées.** Les actions survivent à leurs déclencheurs; le moi se les approprie ensuite.

## Question centrale

Un acte reste-t-il entièrement « mien » si le ressenti décisif, la rencontre, l'interruption et même le moment de fatigue ont été orientés de l'extérieur?

## Conflit politique sans camp moral fixe

Un ange peut produire répression, surprotection ou paralysie au nom de l'ordre; un démon peut provoquer émancipation, innovation ou résistance en brisant un ordre établi. Les démons ne sont pas « gentils » pour autant; les anges ne sont pas « bons » par définition. Les actes ont des conséquences concrètes indépendamment des justifications célestes.

## Protagonistes (proposition)

- **Rupture** : point de vue principal potentiel; plus intéressé par la transformation que par la cruauté.
- **Avarice** : rivalité stratégique; exploite l'accumulation et la dépendance, défend parfois des structures qu'un autre démon veut détruire.
- **Lucifer** : origine historique de la scission; figure d'horizon, de doctrine ou d'arbitrage, à calibrer.
- Les autres entités ont des interventions courtes mais décisives.

## Structure possible

1. **Les déclencheurs** : comprendre la méthode des démons sans exposé doctrinal.
2. **Le prix de l'ordre et de la rupture** : politique, salaire, formation, guerre, prestige, bureaucratie.
3. **Les mécanismes sans maîtres** : le désaccord des démons; les effets échappent aux plans; la question de Dieu reste ouverte.

Ce triptyque est une **hypothèse**, pas une commande de trois actes ni une conclusion imposée.

## Promesse émotionnelle

D'abord un vertige : les grandes décisions ont parfois des déclencheurs minuscules. Puis le calme : cela invite à moins d'orgueil et à plus de compassion, sans effacer les dommages subis ni les responsabilités collectives.

## Contre-modèle

Refuser le roman à thèse où un démon explique le monde en longues tirades pendant que l'histoire attend. Dans chaque chapitre, une **décision irréversible** ou un effet concret précède ou contredit l'idée.

## Le dernier seuil

La fin du **récit** peut demeurer ouverte. Puis un seul paragraphe final, en italique et signé King Klown, relie symboliquement le livre à l'autre univers; aucune mythologie de King Klown dans le corps du roman.

---

## Fichier : `core/02_EDITORIAL_CONTRACT.md`

# Contrat éditorial

## Avec le lecteur

- **Montrer** les chaînes de décisions plutôt que décréter une explication du monde.
- Proposer une double lecture viable : causalités humaines vérifiables et intervention céleste dans la fiction.
- Respecter les personnes ordinaires qui supportent les décisions politiques; ne pas les transformer en simples unités de conséquence.
- Appliquer aux anges et démons la même exigence narrative : sincérité de la mission, aveuglement, effets imprévus.
- L'effet documentaire vient de la **précision vérifiable**, pas d'une fausse présentation du livre comme preuve.

## Priorités éditoriales

**densité causale > tension morale > émotion vécue > exactitude des faits publics > intelligence du dialogue > explication conceptuelle > description**.

Toute scène doit être compréhensible en une lecture, plus riche en deux. La superposition des sens ne doit pas exiger une devinette artificielle.

## Personnes réelles et histoire

- Dates, rôles et décisions publics : **vérifier et dater**; annoter dans `reference/FACT_CHECK_LEDGER.md`.
- Ne pas inventer de citation, de motif intime, de délit ou de confession attribués comme **faits** à une personne vivante.
- Montrer les actes d'un personnage public comme des scènes explicitement **romanesques**, ou utiliser un personnage composite pour toute scène privée très précise.
- Un événement documenté n'est pas la preuve d'une intervention surnaturelle; celle-ci appartient au seul monde fictionnel.
- Pour les sujets contestés (guerres, langues, conscription, conflits d'intérêts), séparer systématiquement faits, interprétations et choix artistiques.

## Symétrie morale sans fausse équivalence

Faire parler Fidélité auprès d'un dirigeant autoritaire ne valide pas sa politique. Mettre un démon auprès d'un chef démocratique ne rend pas ses gestes comparables à ceux d'un agresseur. La force et les effets des actes restent distincts; les forces surnaturelles sont une **grille de fiction**, non une absolution historique.

## Questions à imposer à toute scène

1. Qui veut quoi?
2. Quelle émotion est amplifiée — chez **quelle personne**?
3. Quelle action infime se produit ensuite?
4. Qui la reçoit et comment la convertit-il en autre décision?
5. Quel préjudice et quel bénéfice réels en résultent?
6. Que comprend le lecteur que l'humain ne comprend pas?
7. Quel détail peut disparaître sans perte? Le supprimer.

## Interdits de fabrication

- faux « document secret » revendiqué comme réel;
- monologues pédagogiques qui remplacent une action;
- anges et démons qui soufflent des phrases aux humains;
- télécommande universelle qui élimine toute résistance ou incertitude;
- célébration ou condamnation automatique de toute personne selon son camp politique;
- justifications des dommages sans montrer ceux qui les subissent;
- références à King Klown avant la toute dernière signature.

---

## Fichier : `core/03_VOICE_AND_STYLE.md`

# Voix et style — canon de prose

## Principe

**La phrase sert la bascule.** Pas de description de meubles, de couleur des murs, de météo ou de costumes sans incidence sur le choix ou son ressenti.

La prose n'est **pas** un poème, mais elle emprunte à la poésie la concentration et la possibilité de plusieurs sens. Des paragraphes courts sont possibles; la brièveté ne doit pas devenir une collection d'aphorismes.

## Trois mouvements d'une scène réussie

1. **État initial** : quelqu'un s'apprête à faire un choix concret.
2. **Déviation** : une entité infléchit un *maillon* du réseau, pas nécessairement la personne finale.
3. **Répercussion** : un acte nouveau, un coût humain, une rationalisation a posteriori.

Ne pas dérouler tous les relais si une phrase peut montrer l'essentiel. Un appel n'est pas un hasard commode : une intervention peut avoir rendu l'appel probable.

## Ce que la voix doit éviter

- « Il s'approcha de la fenêtre », « il sourit mystérieusement », « le soleil baignait la pièce » par défaut.
- Apparitions spectaculaires à chaque influence; une entité peut agir sans être décrite physiquement.
- Dialogue humain où l'ange dit « fais ceci »; cela contredit le mécanisme établi.
- Phrases expliquant ce que la scène vient déjà de démontrer.
- Une morale à la fin de chaque chapitre.

## Ce que la voix doit viser

- **Ressentis exacts** : honte, apaisement, répulsion, soulagement, urgence, fatigue, faim de reconnaissance.
- **Relais ordinaires** : une personne qui téléphone, un délai, un rendez-vous annulé, une phrase lâchée, une main qui hésite.
- **Collision d'idéaux** : deux êtres dont les fins semblent nobles mais dont les effets divergent.
- **Causes cumulatives** : la petite influence surnaturelle ne remplace pas l'histoire sociale; elle s'y glisse.
- **Deuxième sens** : la même scène raconte à la fois une chaîne administrative plausible et une manœuvre céleste.

## Dialogues célestes

Les anges et démons **peuvent parler entre eux**. Ils sont intellectuellement cohérents, abstraits, catégoriques; ils ne devraient pas tous débiter les mêmes maximes. Une entité peut reconnaître une perte tactique sans renier son camp.

## Format de travail

Scène-test : **150 à 350 mots** quand l'enjeu le permet; chapitre : longueur dictée par la tension, non par un quota. Réviser d'abord en retranchant 20 % des phrases explicatives. Le vrai critère est la quantité d'effet par phrase, pas le nombre de mots.

## Micro-modèle : chaîne plutôt que décor (non canon)

> Le ministre allait signer. Avarice échouait à l'atteindre : Prudence avait calmé sa peur du changement.
>
> Il choisit un entrepreneur que la réforme inquiétait. À midi, cette inquiétude devint intolérable. L'entrepreneur appela son député.
>
> Un second démon transforma l'hésitation du député en sentiment d'urgence. L'appel fut relayé. Le ministre reporta sa signature pour écouter.
>
> — Tu ne l'as même pas influencé, observa Prudence.
>
> — J'ai influencé le monde qui lui répond, dit Avarice.

Ce fragment illustre une méthode, pas une scène à recopier ni une politique réelle spécifique.

---

## Fichier : `core/04_CHARACTER_BIBLE.md`

# Bible des êtres et des fonctions — propositions encadrées

## Canon commun

- **Démons** : personnages centraux; poursuivent sincèrement une forme de libération et de manifestation divine, avec des méthodes parfois dévastatrices.
- **Anges** : cherchent une cohérence favorable à la manifestation divine; peuvent créer oppression, bureaucratie et immobilisme en poursuivant la protection.
- **Lucifer** : à l'origine de la séparation depuis sa chute avec la moitié des anges; sa psychologie exacte reste à décider.
- **Ni conversion ni changement de camp.** Un désaccord stratégique est possible; un retournement théologique ne l'est pas.
- Leur manière de raisonner est rigide, très abstraite, étrangère à la nuance humaine; éviter d'assimiler ce trait à un diagnostic médical.

## Sept figures démoniaques possibles — PROPOSITION

| Entité | Doctrine / promesse | Action typique | Aveuglement dramatique |
|---|---|---|---|
| **Rupture** | Détruire ce qui fige; permettre la naissance du nouveau | Courage soudain de démissionner; geste qui rompt une alliance | Sous-estime qui paiera le coût de l'effondrement |
| **Avarice** | Affranchir l'accumulation de ses plafonds | Panique devant une perte; soulagement à conserver un avantage | Confond intensification économique et renouveau |
| **Orgueil** | Délivrer l'individu du jugement et de la honte | Blessure narcissique dans une négociation | Transforme une position révisable en identité intouchable |
| **Emprise** | Permettre à la volonté de se matérialiser sans entraves | Besoin de contrôler une information ou un poste | Il recrée l'ordre qu'il prétend briser |
| **Envie** | Rendre toute hiérarchie insupportable | Comparaison soudaine et affront personnel | Détruit la solidarité qui permettrait une réforme |
| **Peur** | Déclencher la réaction qui évite l'immobilisme | Angoisse, urgence, repli | Paralyse autant qu'il mobilise |
| **Indifférence** | Libérer des obligations et attachements paralysants | Insensibilité au dommage éloigné | Ne voit plus les individus derrière les masses |

Rupture et Avarice peuvent former le conflit démoniaque moteur : l'un renverse les institutions, l'autre veut souvent conserver celles qui capitalisent déjà.

## Sept figures angéliques possibles — PROPOSITION

| Entité | Projet cohérent | Dérive possible |
|---|---|---|
| **Prudence** | éviter une rupture destructrice | immobilisme |
| **Concorde** | réunir les intérêts divergents | uniformité forcée |
| **Justice** | garantir des règles applicables | judiciarisation et rigidité |
| **Vigilance** | prévenir les violences et les risques | surveillance généralisée |
| **Compassion** | diminuer la souffrance évitable | paternalisme |
| **Fidélité** | préserver héritages et communautés | interdiction du changement |
| **Courage** | protéger ce qui mérite de durer malgré le coût | sacrifice exigé des autres |

## Humains : fonctions plutôt que portraits psychologiques supposés

Les figures publiques peuvent être des **carrefours de décisions**, sans inventer leurs pensées ni leurs dialogues privés comme des faits. Voir `reference/REAL_PEOPLE_AND_HISTORY.md`. Les personnages composites permettent de dramatiser sans prétendre pénétrer l'intériorité des vivants.

## Limites et décisions ouvertes

- Sept figures par camp? PROPOSITION seulement.
- Rupture comme point de vue récurrent? PROPOSITION.
- Lucifer narrateur, stratège, absent ou antagoniste interne? RÉSERVE.
- Amour entre êtres célestes? Aucun désir romantique canon; ils sont d'abord des êtres de mission.

---

## Fichier : `core/05_THEMES_MOTIFS.md`

# Thèmes et motifs

## Grands thèmes

1. **Choix / réponse** : la conscience se raconte comme auteur d'un geste qu'elle a parfois seulement accueilli.
2. **Bien / coût** : les bonnes intentions d'une entité peuvent produire un dommage grave.
3. **Ordre / ouverture** : protéger peut empêcher d'oser; libérer peut détruire ce qui protège.
4. **Inégalité des prises** : certaines personnes disposent de moins de temps, d'argent ou de réseau pour résister aux circonstances.
5. **Temporalité** : la différence entre deux futurs peut commencer par quatre secondes.
6. **Responsabilité sans souveraineté absolue** : considérer l'influence ne nie pas la nécessité d'enquêter sur les actes et de protéger les victimes.
7. **Déclencheur / récit** : après coup, chaque humain explique l'événement par ses raisons.

## Motifs narratifs (ne pas en faire des tics)

- **L'appel** : non un hasard, mais l'aboutissement d'une chaîne d'émotions chez autrui.
- **La signature retardée** : changer le moment change la suite.
- **Le mot trop vite dit** : le lapsus transforme une négociation.
- **Le geste imperceptible** : une impulsion motrice change une relation.
- **La peur qui se propage** : même sans surnaturel, les réactions contaminent la foule.
- **Le récit après coup** : « c'était ma décision ».
- **La main prêtée** : uniquement comme écho discret, jamais comme annonce de King Klown.

## Motifs à traiter avec retenue

Les « synchronicités », l'inspiration artistique, la conviction soudaine et les coïncidences plausibles peuvent figurer dans la fiction; elles n'y sont **pas la preuve vérifiable** d'une réalité surnaturelle hors du livre.

---

## Fichier : `core/06_CONTINUITY_MAP.md`

# Carte de continuité — version initiale

## Invariants transversaux

- En règle générale, les humains **ne savent pas** que les entités agissent; on ne leur fait pas entendre une voix céleste articulée. Des exceptions conscientes ne sont ni établies ni exclues par le canon.
- Une influence commence dans un contexte précis, souvent une émotion déjà disponible; **pas de pouvoirs illimités**.
- L'intervention peut être chez une **personne tierce**, et la cible ultime ne ressentir aucun contact céleste direct.
- Un blanc de mémoire, un lapsus ou une prise motrice sont possibles, mais ne doivent pas devenir l'explication automatique de tout comportement.
- Deux camps figés depuis Lucifer; alliances tactiques éventuelles au sein d'un camp, **pas de conversion**.
- Les bénéfices et dommages humains continuent d'exister même lorsqu'une entité s'en félicite.
- Sur le plan public : **fait historique → extrapolation déclarée → conséquence humaine**. Ne pas inverser en « source réelle prouve la fiction ».
- Pas de dévoilement de King Klown, Réjean ou de l'univers connexe dans les chapitres.

## Progression proposée (non approuvée)

| Ch. | Acquisition du lecteur | Escalade dramatique | Retenue |
|---:|---|---|---|
| 1–3 | impulsion, relais, relecture de sa décision | premier effet disproportionné | ne pas dévoiler de grande cosmologie |
| 4–6 | économie, réglementation, éducation | conflits internes aux démons | aucune société totalement malveillante |
| 7–9 | tradition, sécurité, médias et guerre | les anges causent parfois des dommages | n'excuser aucune violence réelle |
| 10–12 | réseau, réputation, richesse | les démons font parfois un bien non voulu | éviter la télécommande des dirigeants |
| 13–15 | accumulation de conséquences | l'intérêt d'un démon contredit celui d'un autre | éviter une théorie totale |
| 16–18 | sens de la venue divine; effets sur la responsabilité | issue humaine, incertitude céleste | ne pas fermer philosophiquement le livre |

## Registre de vérification avant prose finale

Tout passage renvoyant à un événement daté : `reference/FACT_CHECK_LEDGER.md` avec preuve ou statut **À VÉRIFIER**. Toute causalité « démoniaque » demeure explicitement du registre romanesque.

---

## Fichier : `core/07_AMBIGUITIES_AND_DECISIONS.md`

# Questions ouvertes et décisions

## CANON (ne pas réouvrir sans demande de l'auteur)

- Protagonistes = démons; anges en contrepoint.
- Chute de Lucifer et de la moitié des anges; camps immuables.
- Influence émotionnelle et parfois corporelle; pas de messages verbaux aux humains.
- Déclencheurs distribués entre personnes; forte densité narrative.
- Réalité documentée extrapolée; effet de quasi-documentaire dans une œuvre de fiction.
- Fin signature de King Klown seule comme lien explicite.

## RÉSERVE : questions créatives significatives

1. **Dieu** : existe-t-il sans ambiguïté pour les entités? A-t-il réellement donné une instruction? Sa « venue » sera-t-elle visible, douteuse ou absente?
2. **Lucifer** : rôle actif, leader distant ou origine symbolique? Peut-il se tromper sur le but tout en restant démon?
3. **Distribution** : exactement sept démons et sept anges? Quels noms seraient définitifs?
4. **Vision** : quel démon porte le plus long fil et prend le plus de décisions risquées?
5. **Portée motrice** : seuil précis de « takeover » et traces après coup; laisser une souplesse tant que les scènes restent cohérentes.
6. **Échelle** : proportion de dirigeants réels versus personnages composites et anonymes.
7. **Dernière partie** : révélation, aporie ou renversement? La paix ne suppose pas un pardon automatique.
8. **Titre** : *Le Conclave des Sept* n'est qu'une étiquette de dossier.

## Arbitrages de v1

- **18 chapitres en 3 mouvements** : **PROPOSITION**, utile pour travailler, pas contrainte fixée par l'auteur.
- **Rupture / Avarice** : antagonisme interne **PROPOSÉ**.
- **Scène d'appel qui décale une décision** : exercice de style **SOURCE DE MÉTHODE**, non évènement imposé dans le manuscrit.
- **Aucune longue exposition initiale** : décision éditoriale dérivée de la préférence explicite pour la densité.

## Registre des modifications

| Date | Décision | Source | Portée |
|---|---|---|---|
| 2026-10-18 | Canon d'influence, ton, protagonistes, deux camps, dernière signature | échange auteur | tous les chapitres |
| 2026-10-18 | organisation documentaire à la manière de `Colin_Row.zip` | dépôt de référence fourni | arborescence uniquement |

---

## Fichier : `core/08_WRITING_PROTOCOL.md`

# Protocole de rédaction

## Avant une scène

1. Lire `00_CANONICAL_STATE`, `03_VOICE_AND_STYLE`, `12_INFLUENCE_MECHANICS`, le brief et `06_CONTINUITY_MAP`.
2. Écrire la chaîne en une ligne : **réceptivité A → émotion A → action A → information/événement B → réaction C → effet**.
3. Écrire séparément la lecture « humaine ordinaire » de la chaîne : elle doit rester plausible.
4. Nommer le conflit d'objectifs des entités; aucune ne veut « le mal pour le mal ».
5. Si scène publique historique : relever précisément ce qui est fait, supposé, ou inventé.

## Pendant

- Entrer **près du choix**; pas de prologue spatial.
- Écrire des **sensations et des gestes**, non des explications télépathiques.
- Si une entité parle, elle s'adresse à une autre entité; pas de monologue-cours.
- Couper les déplacements et les gestes sans effet causal.
- Montrer au moins **une conséquence** (y compris pour un tiers invisible aux puissants).

## Après

- Supprimer 20 % des explications; supprimer tout décor indifférent au dilemme.
- Repérer le double sens : qu'apprend le lecteur sur l'humain **et** sur l'entité?
- Tester la symétrie morale : l'ange a-t-il une raison honnête? le démon a-t-il une raison honnête? Les victimes existent-elles toujours dans le texte?
- Vérifier la continuité : pas de conversion, pas de « mots envoyés », pas de présence King Klown.
- Mettre le chapitre dans `manuscript/` **seulement après validation**, les variantes dans `working/`.

## Test des cinq phrases

Décrire en cinq phrases : situation, première influence, relais, bascule, coût. Si ce résumé est confus, le chapitre n'est pas assez pensé pour être développé.

## Niveaux d'affirmation

- **Réalité attestée** : source à consigner.
- **Inférence discutée** : présentée comme interprétation.
- **Invention** : clairement l'une des conventions du roman.

Aucun manque de preuve ne doit être comblé par « les démons l'ont forcément fait » présenté comme événement extérieur à la fiction.

---

## Fichier : `core/09_CHAINES_DE_CAUSALITE.md`

# Chaînes de causalité — moteur original du roman

## Principe

Une intervention réussie peut ne toucher **aucunement la cible finale**. Les démons savent que les êtres humains vivent en réseau; modifier un maillon modifie le trajet. La réalité ordinaire fournit déjà fatigue, pression, information inégale, hiérarchie, contacts et délais.

## Chaîne A — L'appel qui retarde

**Enjeu :** politique économique ou réforme.

Entrepreneur inquiet → amplification d'urgence → appel au député → sentiment d'importance chez le député → transmission à une conseillère → réunion interrompue → signature reportée → fenêtre politique fermée.

**Version observable :** consultations, pressions, remaniement du calendrier.

**Version céleste :** le démon n'a jamais influencé directement le ministre.

**Contrepoids :** le règlement pouvait avoir des coûts réels; Prudence ne cherchait pas gratuitement la paralysie.

## Chaîne B — L'entretien d'embauche

Candidat de milieu modeste → fatigue après quart de travail → micro-irritation dans une réponse → impression négative chez recruteur → offre à une candidate déjà connue → nouveau contact au sommet trois ans plus tard.

**Version observable :** asymétrie de préparation, références et réseaux.

**Version céleste :** Orgueil peut n'amplifier qu'une minute de gêne.

**Contrepoids :** ne pas supposer absence de mérite chez l'autre candidate.

## Chaîne C — La grève

Un employé humilié → conviction de ne plus rien devoir → paroles exactes au bon moment → collègues se coordonnent → grève → hausse salariale possible / fermeture possible.

**Version observable :** organisation syndicale et contraintes économiques.

**Version céleste :** Rupture gagne une ouverture; Prudence protège l'emploi existant.

**Contrepoids :** travailleurs aux intérêts différents, effets collatéraux et bénéfices non garantis.

## Chaîne D — Le mot irréparable

Conférence internationale → interprète fatigué → lapsus de nuance → humiliation ressentie chez interlocuteur → position durcie → communiqué modifié → nouvelle crise.

**Version observable :** chaîne diplomatique complexe.

**Version céleste :** Envie/Orgueil cible une émotion secondaire plutôt qu'une volonté présidentielle.

**Contrepoids :** éviter d'attribuer une crise historique réelle à un lapsus inventé sans signal romanesque.

## Chaîne E — Le geste sauveur

Une automobiliste ressent un brusque mouvement de recul → freine avant de voir l'enfant → collision évitée → un autre automobiliste derrière elle est blessé.

**Version observable :** réflexe et attention distribuée.

**Version céleste :** Compassion a sauvé quelqu'un sans pouvoir garantir l'absence de dommage.

**Contrepoids :** un bénéfice ne rend pas toute méthode juste.

## Chaîne F — La règle protectrice

Accident réel → indignation collective → vigilance institutionnelle → norme plus stricte → incident évité → coûts de conformité → petites structures exclues → concentration des acteurs.

**Version observable :** compromis réglementaire difficile.

**Version céleste :** Justice protège et, à son insu, peut favoriser Avarice.

**Contrepoids :** ne pas confondre toute réglementation avec oppression.

## Chaîne G — Une information enterrée

Employé documente un abus → supérieur craint le désordre → signalement retardé → journaliste reçoit un fragment → décision publique sous information incomplète.

**Version observable :** inertie administrative, secret professionnel et stratégie médiatique.

**Version céleste :** Concorde étouffe un conflit qu'Envie déchaîne ensuite.

**Contrepoids :** le secret peut parfois aussi protéger les personnes.

## Usage

Chaque chapitre devrait posséder une chaîne équivalente **sans recopier** ce catalogue. Une chaîne n'est pas une théorie complète du monde : elle est le mécanisme local d'un récit.

---

## Fichier : `core/10_CHAPTER_ENGINE.md`

# Moteur de chapitre — v1 (plan proposé)

Chaque chapitre fait avancer simultanément :

1. **conflit entre entités** : désaccord de finalité ou de moyen;
2. **décision humaine** : une bascule observable;
3. **chaîne d'influences** : au moins un maillon pertinent;
4. **problème moral** : bien selon l'un, mal selon l'autre, coût concret;
5. **question métaphysique** : un doute qui s'accumule au lieu d'être répété.

| Ch. | Fonction dominante | Protagoniste proposé | Question pendante |
|---:|---|---|---|
| 1 | effet d'une infime impulsion | Rupture | d'où vient une décision? |
| 2 | agir à travers autrui | Avarice | qui est réellement visé? |
| 3 | récit qu'on fait après coup | Orgueil | que signe le moi? |
| 4 | salaire et dépendance | Avarice/Rupture | sécurité ou captivité? |
| 5 | diplôme et sélection | Envie/Prudence | mérite ou condition d'accès? |
| 6 | loi protectrice et inertie | Rupture/Justice | protéger sans bloquer? |
| 7 | traditions et coercition | Emprise/Fidélité | préserver ou imposer? |
| 8 | sécurité et libertés | Peur/Vigilance | peur justifiable? |
| 9 | guerre et sacrifice | Orgueil/Courage | qui peut exiger le prix? |
| 10 | patrimoine et réseaux | Avarice/Concorde | qui entre dans la salle? |
| 11 | médias et émotion publique | Envie/Justice | qu'a-t-on vu vraiment? |
| 12 | invention et rupture | Rupture/Prudence | coût acceptable du nouveau? |
| 13 | compétition entre démons | Avarice/Rupture | chaos ou capitalisation? |
| 14 | l'ange produit un dommage | Justice | une bonne règle peut-elle nuire? |
| 15 | le démon produit un bien | Rupture | un mal projeté reste-t-il mal? |
| 16 | l'échec d'un calcul céleste | Peur/Compassion | qui maîtrise les conséquences? |
| 17 | l'objectif de la venue | Lucifer / collectif | Dieu veut-il cela? |
| 18 | responsabiliser sans condamner entièrement | collectif démoniaque | qu'a-t-on vraiment choisi? |

Chapitres = **fiches d'orientation remplaçables**, non promesse d'une liste de faits historiques précis.

## Règle d'issue

Terminer par une bascule **émotionnelle ou causale**, pas une formule philosophique obligatoire. Une scène documentaire n'est pas une page de doctrine.

---

## Fichier : `core/11_CANON_DECISIONS_V1.md`

# Registre des décisions — v1

| Sujet | Contenu | Statut |
|---|---|---|
| Protagonistes | Démons | CANON |
| Anges | Contrepartie structurante, vertus pouvant se retourner | CANON |
| Origine | Chute de Lucifer avec moitié des anges; camps permanents | CANON FICTION |
| Motivations | Chaos/rupture pour une manifestation divine, ordre pour l'autre conception | CANON D'ORIENTATION |
| Communication | Émotions, intuitions, impulsions; pas de phrases vers humains | CANON |
| Influence corporelle | lapsus, blancs, mouvements, perte émotionnelle de contrôle, cas limités | CANON QUALITATIF |
| Réseau | influencer l'appelant peut être plus efficace qu'influencer le ministre | CANON |
| Genre | histoire libre, ancrée dans réalité extrapolée; quasi documentaire | CANON |
| Densité | prose ramassée, sensations, causalité, doubles sens | CANON |
| Finalité lecteur | ébahi puis en paix; relativisation de souveraineté morale | CANON |
| Signature | Colin Row en couverture; toute dernière note King Klown / Réjean | CANON |
| Titre | Le Conclave des Sept | PROPOSITION |
| Sept figures de chaque côté | distribution de travail | PROPOSITION |
| Plan | 3 parties, 18 chapitres | PROPOSITION |
| Rupture centre | fil démoniaque dominant | PROPOSITION |
| Révélation divine | visible ou non? | OUVERT |
| Personnes réelles citées | casting sélectif selon événements publics vérifiés | OUVERT |

---

## Fichier : `core/12_INFLUENCE_MECHANICS.md`

# Mécanique d'influence — règles à tester en scène

## Énoncé canonique

Une entité **ne commande pas avec des mots** : elle rend soudain une issue attirante, répugnante, urgente, rassurante ou insupportable. L'humain ressent; il réagit; il donne ensuite un sens à son geste.

## Spectre d'action (qualitatif, non chiffré)

1. **Coloration** : une opinion devient plus apaisante, une option plus lourde.
2. **Impulsion** : appel, silence, mot, regard ou départ au moment charnière.
3. **Perturbation** : lapsus, blanc, attention déplacée, mémoire trouée.
4. **Prise passagère** : émotion qui déborde et guidage moteur court. Le sujet peut ensuite se demander pourquoi il a agi ainsi.

Les quatre ne doivent pas être perçus comme des « sorts » à invoquer en séquence; c'est une échelle narrative pour la continuité.

## Réceptivité

- Tout humain est influençable **jusqu'à un certain point**, jamais identiquement.
- L'efficacité dépend du moment, de l'état émotionnel, des habitudes, des motivations préexistantes et du nombre de relais.
- Aucun « contrôle permanent » n'est canonique.
- Les êtres savent sélectionner les instants où l'humain a déjà de bonnes raisons **humaines** d'aller dans une direction.

## Influence distribuée

Forme standard : `A ressent → A agit → B reçoit → B interprète → C répond → système bifurque`.

Les entités peuvent se disputer **le maillon** plutôt que le dirigeant. Éviter qu'elles soient omniprésentes : choisir un seul point d'appui suffisamment décisif.

## Ce que le narrateur sait

Il peut dévoiler la manœuvre céleste au lecteur. Il ne doit pas transformer les constats réels en preuves du surnaturel. Les protagonistes peuvent surestimer leur pouvoir ou revendiquer des effets qu'ils n'ont pas causés.

## Questions encore ouvertes

- Y a-t-il une limite au nombre d'humains touchés simultanément?
- Quels sont les coûts d'une prise motrice intense?
- Peut-on contre-influencer la même personne dans le même instant?
- L'esprit humain a-t-il un noyau inaccessible, ou la limite n'est-elle qu'une question de circonstances?

**Ne pas inventer des lois universelles tant qu'une scène n'en a pas réellement besoin.**

---

## Fichier : `core/13_ENDING_PROTOCOL.md`

# Protocole de fin — lien discret à l'univers King Klown

## CANON

L'auteur de couverture est **Colin Row**, pseudonyme de l'auteur. Le livre n'expose **pas** l'univers King Klown. Le dernier élément imprimé, **après la fin du récit**, est un bref paragraphe **en italique** où King Klown remercie Réjean McCormick de lui avoir prêté ses mains pour composer ce livre. Rien après ce paragraphe.

## Formulation de travail (fidèle à l'idée de l'auteur)

*Je remercie Réjean McCormick de m'avoir prêté ses mains pour composer ce livre.*

*— King Klown*

L'auteur peut modifier les mots; la **fonction** demeure. Il s'agit d'une **mise en abyme de fiction**, pas d'une assertion à étayer sur une prise de possession dans la réalité.

## À ne pas faire

- annoncer King Klown dans un chapitre;
- révéler une cosmogonie King Klown;
- expliquer la note ou l'incarnation aux lecteurs;
- mettre un épilogue analytique, une morale ou un glossaire après la note;
- forcer des indices « mains empruntées » à chaque scène pour fabriquer le twist.

La mécanique des autres livres peut fournir le contexte à ceux qui les connaissent. Ce livre n'a pas à enseigner leur lore.

---

## Fichier : `core/14_STORY_ENGINE.md`

# Moteur dramatique — comment faire un roman plutôt qu'un catalogue

**Statut : PROPOSITION de méthode.** Ce document n'ajoute aucun événement au canon.

## Unité narrative

Une scène n'existe que si elle modifie **au moins deux** de ces états :

1. une situation humaine réelle (qui peut agir, perdre, attendre, aimer, payer);
2. l'avantage relatif d'une entité (qui a obtenu un relais ou perdu une possibilité);
3. la connaissance du lecteur (ce qu'il croit être la source d'un choix);
4. la relation entre démons (rivalité doctrinale ou dette stratégique);
5. une chaîne qui portera ses effets ailleurs, plus tard.

**Formule condensée** : désir humain disponible → infime perturbation ciblée → relais plausible → choix interprété comme volontaire → conséquence coûteuse → récupération stratégique / erreur céleste.

## Le moteur de la suite

Chaque chapitre doit léguer une **conséquence active**, et non seulement une idée, à un chapitre ultérieur. Par exemple :

- une réforme reportée accroît la pression sur une employée;
- sa réaction déplace une embauche;
- cette embauche crée un réseau de confiance;
- ce réseau affecte une institution;
- la décision institutionnelle déplace des milliers de vies.

L'ordre est modulable. Chaque flèche est **une hypothèse fictionnelle**, à justifier par des intérêts humains intelligibles. Éviter que toutes les crises du monde viennent d'une seule chaîne parfaite.

## Ce qu'un démon veut, ce qui l'arrête

Pour chaque démon dans chaque scène, formuler deux propositions contradictoires :

- **Sa vérité** : ce que la mission lui fait tenir pour bon.
- **Sa difficulté concrète** : le fait humain qui résiste à sa vérité.

Exemple, Avarice : l'accumulation donne les moyens d'inventer des mondes nouveaux; pourtant, l'outil d'accumulation peut rendre les humains incapables de risquer ce qu'ils possèdent. Ce conflit n'exige pas une conversion de camp.

## Séquences de reprise

Ne pas montrer sept fois le même « moment d'impulsion ». Alterner :

- **Action révélée** : le lecteur voit l'entité agir, puis la décision publique.
- **Action reconstruite** : le lecteur voit l'effet avant de découvrir le relais.
- **Action ratée** : une impulsion ne prend pas, et une autre cause l'emporte.
- **Action disputée** : deux entités visent deux relais opposés; résultat non prévu.
- **Fausse attribution** : un démon revendique un succès qu'il n'a pas causé.
- **Contrecoup** : ce qui ressemblait à un échec permet le prochain succès d'autrui.

Ne jamais nommer ces catégories dans le manuscrit.

## Test de non-redondance

Si deux scènes peuvent échanger leurs noms et rester identiques, une des deux doit changer de **mécanisme**, de **coût**, de **bénéficiaire**, ou disparaître.

Si un chapitre est supprimé, doit-on perdre autre chose qu'un argument? Si la réponse est non, c'est probablement un passage d'essai à déplacer dans `reference/`.

## Fin de roman

Aucune solution métaphysique obligatoire. Le récit doit parvenir à un fait ou à une décision qui fasse ressentir la diminution de la souveraineté morale **sans** retirer aux victimes leur réalité ni transformer les humains en automates sans intérêt. La note King Klown est **hors récit**, traitée dans `13_ENDING_PROTOCOL.md`.

---

## Fichier : `core/15_GRAMMAIRE_DES_INFLUENCES.md`

# Grammaire de l'influence — précision sans magie explicative

**Statut : CANON sur les capacités déjà fixées; PROPOSITION sur les tests et classifications ci-dessous.**

## Les deux niveaux de cause

**Plan visible** : les faits ordinaires suffisent à expliquer pourquoi un appel est passé, pourquoi une colère éclate, pourquoi une signature attend.

**Plan romanesque** : une entité a orienté une émotion ou une action suffisamment tôt pour modifier la chaîne. Elle ne remplace pas la causalité humaine, elle l'utilise.

Un événement peut être rendu **plus probable**, non nécessairement certain. Ne pas donner aux entités la maîtrise de toutes les suites.

## Trois leviers qui ne sont pas des ordres verbaux

| Levier | Chez l'humain | Exemple court | Risque littéraire |
|---|---|---|---|
| Valence | une issue paraît soudain juste / répugnante | conserver son emploi lui apporte un soulagement imprévu | psychologie transformée en télécommande |
| Intensité | sentiment existant amplifié au point de déclencher un acte | une inquiétude devient urgente; il appelle | crise émotionnelle démesurée et répétitive |
| Fenêtre | attention, mémoire ou mot dérive au moment décisif | un rendez-vous est pris aujourd'hui plutôt que demain | hasard artificiellement surnaturel |

Le **guidage bref du corps**, les lapsus et les blancs de mémoire appartiennent aux possibilités déjà fixées, mais doivent rester des cas singuliers : ils coûtent en crédibilité s'ils expliquent tout.

## Le relais comme centre de gravité

Ne pas commencer par « Comment changer la volonté du ministre? » mais par « Qui peut lui modifier une circonstance? »

Exemple : peur chez A → appel à B → impression d'urgence chez B → interruption de C → hésitation de C → ajournement. Un seul chaînon suffit parfois. Montrer **le maillon déterminant**, pas forcément tous.

## Les quatre tests avant d'approuver une influence

1. **Ancrage** : quelle vulnérabilité était déjà présente? (fatigue, fidélité, réputation, dette, protection d'un proche).
2. **Économie** : quel est le plus petit levier suffisant? Une main guidée est rarement nécessaire.
3. **Résistance** : qu'aurait pu faire cette personne autrement? La scène doit laisser un espace de friction.
4. **Double lecture** : sans les entités, l'enchaînement reste-t-il humainement crédible?

## Contrefactuel local

Chaque chaîne de scène doit répondre en une phrase à : **sans l'intervention, quel est le déroulement le plus plausible?** Ce n'est pas une preuve de l'effet; c'est un test de nécessité dramatique. Si le monde aurait évolué exactement de la même manière, couper la manœuvre ou changer sa cible.

## Ce qui reste ouvert

Les limites physiques précises, la simultanéité, les coûts de prise motrice, la possibilité pour deux entités d'influencer un même humain à la milliseconde, et la connaissance de l'avenir **ne sont pas arrêtés**. Aucune scène-test ne peut les canoniser tacitement.

---

## Fichier : `core/16_DOCTRINES_EN_CONFLIT.md`

# Doctrines en conflit — donner à chaque entité sa nécessité

**Statut : PROPOSITION de caractérisation.** Les noms et le compte des figures restent révisables. Les camps, eux, sont fixes.

## Les démons : divergences irréductibles, fidélité intacte au camp

| Démon | Le bien qu'il pense servir | Le geste qu'il privilégie | Ce qu'un autre démon lui reproche | Une contradiction à jouer |
|---|---|---|---|---|
| Rupture | faire advenir l'imprévu nécessaire à la manifestation de Dieu | interrompre, délier, provoquer le départ | Avarice : « Tu détruis nos prises » | le chaos favorise parfois les déjà-puissants |
| Avarice | décupler la capacité humaine d'agir par les ressources | accroître la peur de perdre, retenir | Rupture : « Tu fabriques des prisons » | la conservation des richesses étouffe le renouveau |
| Orgueil | soustraire l'individu à la soumission et à la honte | rendre un recul humiliant | Emprise : « Tu rends nos alliés imprévisibles » | la volonté de ne jamais céder produit de nouvelles chaînes |
| Emprise | rendre efficace une volonté contre les résistances | créer réseau, dépendance, contrôle | Rupture : « Tu rebâtis des murs » | son moyen ressemble à l'ordre angélique |
| Envie | rendre une hiérarchie insoutenable | déclencher comparaison, soupçon | Indifférence : « Tu attaches encore les hommes aux autres » | la division peut défendre la hiérarchie |
| Peur | forcer l'action avant qu'il ne soit trop tard | transformer souci en urgence | Orgueil : « Tu rends les humains lâches » | la panique donne du pouvoir aux protecteurs de l'ordre |
| Indifférence | délier des devoirs qui empêchent l'expérimentation | diminuer la gêne devant un coût lointain | Rupture : « Tu coupes jusqu'au désir de changer » | sans attachement, qui voudra bâtir le nouveau? |

## Les anges : finalité collective, dommages possibles

| Ange | Le bien qu'il pense servir | Son outil | Sa dérive possible |
|---|---|---|---|
| Prudence | éviter les pertes irréversibles | réticence, anticipation | paralyser |
| Concorde | accorder les personnes | apaisement, loyauté | étouffer la dissidence |
| Justice | protéger contre l'arbitraire | cohérence et obligation | multiplier les règles |
| Vigilance | détecter le danger | alerte et protection | installer la surveillance |
| Compassion | réduire la souffrance | proximité affective | retirer aux autres leur autonomie |
| Fidélité | garder ce qui relie les générations | attachement, honneur | contraindre au nom de la tradition |
| Courage | soutenir une protection coûteuse | fermeté, endurance | imposer le sacrifice à autrui |

## Faire sentir leur étrangeté

Ils ne sont pas des humains déguisés. Une entité peut regretter **une inefficacité**, non ressentir spontanément la culpabilité humaine. Son raisonnement a des angles morts cohérents, et son langage peut être rapide, presque géométrique.

Ne pas utiliser « autiste » comme raccourci descriptif d'une absence d'empathie : écrire plutôt **absolu, monomaniaque, inflexible, incapable de tolérer une contradiction de doctrine**.

## Nœuds de rivalité à répéter avec variation

- Rupture / Avarice : détruire un monopole ou préserver une machine d'accumulation?
- Emprise / Orgueil : discipliner les chefs ou leur donner le goût d'être indomptables?
- Peur / Indifférence : augmenter l'attachement à ce qui se perd ou supprimer cet attachement?
- Prudence / Compassion : protéger la structure ou soulager immédiatement ceux qui y souffrent?
- Justice / Fidélité : une règle juste peut-elle rompre une coutume précieuse?

**Interdiction dramatique :** résoudre une rivalité par une conversion de camp. Une coopération locale ne change pas la nature d'un ange ou d'un démon.

---

## Fichier : `core/17_COURBE_DU_LECTEUR.md`

# Courbe de lecture — du « c'est banal » au « comment ai-je choisi? »

**Statut : PROPOSITION narrative; non chronologie canonique.**

## La promesse à chaque seuil

| Seuil | Ce que voit le lecteur | Ce qu'il reconsidère | Danger d'écriture |
|---|---|---|---|
| Ouverture | un acte ordinaire, un ressenti, un minuscule décalage | l'origine d'une décision | scène d'exposition métaphysique |
| Première conséquence | une série de relais produit un effet disproportionné | la causalité individuelle | « tout arrive par magie » |
| Premier revers | un démon fait naître une amélioration, un ange cause un dommage | le classement bien / mal | morale relativiste simpliste |
| Milieu | les démons ne s'accordent pas sur la même stratégie | qui tient les fils? | répétition des discours |
| Renversement | une manœuvre réussie échoue à long terme ou est revendiquée à tort | la maîtrise des entités elles-mêmes | surpuissance puis retcon |
| Sortie | le lecteur ressent simultanément lucidité et compassion | responsabilité moins absolue | « rien n'importe, personne n'est responsable » |

## L'expérience d'un chapitre

Chaque chapitre doit laisser **au moins une question pratique** ouverte : qui doit réparer le dommage? qui bénéficie de la règle? pourquoi cet appel maintenant? Il n'a pas à se terminer sur un aphorisme.

La paix finale n'est pas la certitude que personne n'est responsable; elle vient de la possibilité de **juger moins vite tout en continuant de protéger les personnes blessées**.

## Densité sans obscurité

- Une phrase peut cumuler un fait, un ressenti et une causalité invisible.
- Deux lectures superposées sont préférables à une énigme insoluble.
- Après une séquence abstraite, donner un coût concret (temps, revenu, relation, vie, réputation).
- Si un nouveau concept prend un paragraphe pour être exposé, l'essayer d'abord dans un choix.

## La dernière page

La dernière scène du **roman** n'annonce pas King Klown. Le remerciement en italique est imprimé après la fin et **n'exige aucune préparation doctrinale interne**, conformément à la décision ultérieure de l'auteur.

---

## Fichier : `core/18_CONTINUITE_CAUSALE.md`

# Continuité causale — ne pas confondre influence et omnipotence

**Statut : OUTIL de travail.**

## Journal minimal par bascule

| Champ | Question |
|---|---|
| ID | Identifiant stable `E01`, `E02`… |
| Déclencheur observable | Quelle circonstance ouvre la scène? |
| Prise invisible | Qui agit, sur qui, par quel **ressenti**? |
| Acte observable | Qu'a fait effectivement la personne? |
| Explication ordinaire | Quelles raisons non surnaturelles suffisent à comprendre l'acte? |
| Coût et bénéfice | Qui perd quelque chose? Qui gagne quelque chose? |
| Contrefactuel | Que se serait-il probablement passé sans cette influence? |
| Effet différé | Dans quel chapitre retrouve-t-on la conséquence? |
| Statut de vérité | fait public vérifié / fiction / lecture controversée |

## Relations interdites par le canon

- une entité transmet un long discours articulé à un humain;
- un ange devient démon ou l'inverse;
- une influence provoque une action indépendamment de toute prise ou tout contexte humain, comme une télécommande illimitée;
- l'auteur utilise la note King Klown pour expliquer rétroactivement l'intrigue;
- un personnage réel est décrit comme possédé **dans la réalité**, hors du dispositif de fiction.

## Relations permises, non obligatoires

- l'entité influence un tiers plutôt que la personne décisive;
- un effet indirect a lieu des années après une intervention;
- le même événement bénéficie à un ange et à un démon pour des raisons différentes;
- un démon attribue à tort un résultat à sa propre intelligence;
- plusieurs plans causaux vrais dans le récit se superposent.

## Invariant sur l'histoire réelle

Pour un événement réel mentionné, conserver la distinction : **chronologie documentée / motivations publiques attribuées / désaccords d'interprétation / mécanisme fantastique inventé**. Un narrateur très sûr de lui peut être un démon **peu fiable** : cette assurance n'est pas la validation documentaire d'une thèse.

---

# Parties proposées

## Fichier : `parts/PART_1_LES_DECLENCHEURS.md`

# Partie I — Les déclencheurs (PROPOSITION)

## Fonction

Faire comprendre le fonctionnement des influences **par l'effet avant la doctrine**. Le premier chapitre ne récite ni la chute de Lucifer, ni un traité métaphysique. Il montre une décision prise « librement », puis la chaîne qui l'a rendue possible.

## Mouvement

- Des actes infimes modifient les vies.
- Les démons ont des tempéraments et des stratégies non interchangeables.
- Les anges produisent parfois des protections réelles, mais à un prix.
- Les humains reconstruisent a posteriori leur récit d'autonomie.

## Sortie recherchée

Le lecteur reconnaît un incident ordinaire et saisit qu'il est désormais capable de le lire de deux manières. Il veut suivre **les démons**, pas seulement deviner un twist.

## Règle

Six chapitres **proposés**, pas une forme fixée. Aucun exposé cosmologique long. L'origine des camps peut surgir dans un désaccord bref, plus tard.

---

## Fichier : `parts/PART_2_LE_PRIX_DES_VERTUS.md`

# Partie II — Le prix des vertus (PROPOSITION)

## Fonction

Faire franchir au roman une échelle : de l'emploi, de la formation et du règlement à des décisions publiques plus vastes. Montrer des cas où la protection angélique produit un dommage, et où la rupture démoniaque permet parfois un bien.

## Principe

Un cas contemporain documenté **n'est jamais une preuve d'une intervention céleste réelle**. Le roman peut greffer sa chaîne imaginaire sur des faits publics, mais ses causalités surnaturelles restent fictives.

## Mouvement

- Identité collective et coercition possible.
- Sécurité et libertés civiles.
- Guerre, conscription, défense, coûts humains sans raccourcis causaux.
- Transmissions de privilèges et réputation.
- Médias, perception et décision.
- Création contre protection.

## Sortie recherchée

Les catégories « ange = bien » et « démon = mal » ont cessé de fonctionner; personne n'est absous, personne n'est condamné par étiquette.

---

## Fichier : `parts/PART_3_LE_MONDE_SANS_MAITRES.md`

# Partie III — Le monde sans maîtres (PROPOSITION)

## Fonction

Les démons découvrent qu'ils ne maîtrisent ni toutes les causes ni toutes les conséquences, même lorsqu'ils orientent des relais décisifs. Leurs interprétations de la venue divine s'affrontent à des faits humains qui les dépassent.

## Trajectoire

- Avarice conserve ce que Rupture veut renverser.
- Une règle angélique protège et concentre simultanément.
- Un geste démoniaque de destruction permet une émancipation.
- Une influence aboutit à l'inverse de sa fin.
- Le problème de Dieu et de la responsabilité cesse d'être seulement théorique.

## Sortie recherchée

**Ébahissement sans paranoïa**; la fin aide à comprendre plutôt qu'à accuser indistinctement. L'éventuelle présence de Dieu reste **ouverte** dans le plan de travail.

## Après le récit

Un seul paragraphe final, en italique, signé King Klown. Aucun lien à cet univers n'est explicité auparavant.

---

# Fiches de chapitre proposées

## Fichier : `chapter_briefs/01_la_seconde_de_trop.md`

# Chapitre 1 — La seconde de trop

**Statut : PROPOSITION**, non canon narratif.

## Partie / focalisation

Partie 1. **Entités :** Rupture / Prudence.

## Situation initiale

Un employé manque de perdre le contrôle lors d’un entretien disciplinaire; une fraction de seconde change la décision.

## Chaîne de nécessité

Fatigue, rapport d’autorité, honte; émotion orientée juste avant la réponse.

## Deux lectures superposées

Le geste paraît psychologiquement plausible; le lecteur voit le déclencheur invisible.

## Travail du chapitre

Faire connaître Rupture par une décision, non par une biographie céleste.

## Risque / contrepoids

La même seconde peut déboucher sur une dénonciation courageuse ou une faute. Ne pas fixer le résultat moral trop tôt.

## Écriture

Entrer au moment de la bascule. Aucune mise en scène décorative. Une émotion précise, un relais crédible, un effet humain visible. **Les entités se parlent entre elles, pas aux humains.**

## Sortie cherchée

Le lecteur comprend une **conséquence**, mais ne reçoit ni morale définitive ni certitude que l'entité a prévu toute la chaîne.

## Spécificité dramatique — PROPOSITION v2

- **Levier distinctif :** Rupture amplifie une honte déjà active chez une salariée; une phrase qu'elle retenait sort trop tôt.
- **Prix immédiat :** Elle s'expose, mais révèle une pratique; l'emploi devient précaire.
- **Écho à construire :** Le chapitre 4 peut reprendre le prix de ce geste et le chapitre 15 sa portée inattendue.
- **Question à préserver :** Si ce mot était resté tu, un autre témoin aurait-il parlé?

---

## Fichier : `chapter_briefs/02_les_relais.md`

# Chapitre 2 — Les relais

**Statut : PROPOSITION**, non canon narratif.

## Partie / focalisation

Partie 1. **Entités :** Avarice / Prudence.

## Situation initiale

Un appel d’une personne périphérique modifie le calendrier d’une décision officielle.

## Chaîne de nécessité

Inquiétude chez A → appel à B → sentiment d’urgence chez B → C interrompt D → D reporte.

## Deux lectures superposées

Pression politique ordinaire / manœuvre émotionnelle distribuée.

## Travail du chapitre

Enraciner la règle : le destinataire final peut ne subir aucune influence directe.

## Risque / contrepoids

Ni le ministre ni l’entreprise ne sont présumés malveillants; les coûts de la réforme demeurent débattables.

## Écriture

Entrer au moment de la bascule. Aucune mise en scène décorative. Une émotion précise, un relais crédible, un effet humain visible. **Les entités se parlent entre elles, pas aux humains.**

## Sortie cherchée

Le lecteur comprend une **conséquence**, mais ne reçoit ni morale définitive ni certitude que l'entité a prévu toute la chaîne.

## Spécificité dramatique — PROPOSITION v2

- **Levier distinctif :** Avarice atteint une décision institutionnelle en déclenchant chez un tiers la peur de perdre.
- **Prix immédiat :** Un appel interrompt un processus sans que la cible finale soit directement influencée.
- **Écho à construire :** Le report peut créer le contexte réglementaire du chapitre 6.
- **Question à préserver :** Ne pas présumer qu'un simple appel entraîne nécessairement un renversement.

---

## Fichier : `chapter_briefs/03_le_choix_apres_coup.md`

# Chapitre 3 — Le choix après coup

**Statut : PROPOSITION**, non canon narratif.

## Partie / focalisation

Partie 1. **Entités :** Orgueil / Compassion.

## Situation initiale

Une personne donne a posteriori une explication cohérente à un acte qui l’a elle-même surprise.

## Chaîne de nécessité

Humiliation perçue → lapsus → lien rompu → récit justificatif.

## Deux lectures superposées

Rationalisation psychologique / impulsion accentuée par un démon.

## Travail du chapitre

Faire ressentir sans commentaire professoral la différence entre agir et s’en dire auteur.

## Risque / contrepoids

Ne pas présenter les pertes de mémoire comme preuve surnaturelle hors de la fiction.

## Écriture

Entrer au moment de la bascule. Aucune mise en scène décorative. Une émotion précise, un relais crédible, un effet humain visible. **Les entités se parlent entre elles, pas aux humains.**

## Sortie cherchée

Le lecteur comprend une **conséquence**, mais ne reçoit ni morale définitive ni certitude que l'entité a prévu toute la chaîne.

## Spécificité dramatique — PROPOSITION v2

- **Levier distinctif :** Une personne attribue un refus impulsif à ses « valeurs », puis réécrit sa biographie autour de ce moment.
- **Prix immédiat :** L'entité revendique le déclencheur, mais la personne porte la conséquence.
- **Écho à construire :** Faire revenir cette rationalisation au chapitre 18, sans explication définitive.
- **Question à préserver :** Que sait réellement l'entité du motif de la personne?

---

## Fichier : `chapter_briefs/04_le_salaire_du_depart.md`

# Chapitre 4 — Le salaire du départ

**Statut : PROPOSITION**, non canon narratif.

## Partie / focalisation

Partie 1. **Entités :** Avarice / Rupture / Compassion.

## Situation initiale

Une négociation salariale confronte la survie de l’entreprise à la possibilité réelle de démissionner.

## Chaîne de nécessité

Réserve de trésorerie du salarié → peur de partir → offre acceptée → dépendance accrue.

## Deux lectures superposées

Marché du travail, pouvoir de négociation / polarisation de ressentis.

## Travail du chapitre

Distinguer liberté légale de partir et ressources pour le faire.

## Risque / contrepoids

Le salaire bas n’est pas toujours choisi pour soumettre; montrer aussi contraintes et concurrence.

## Écriture

Entrer au moment de la bascule. Aucune mise en scène décorative. Une émotion précise, un relais crédible, un effet humain visible. **Les entités se parlent entre elles, pas aux humains.**

## Sortie cherchée

Le lecteur comprend une **conséquence**, mais ne reçoit ni morale définitive ni certitude que l'entité a prévu toute la chaîne.

## Spécificité dramatique — PROPOSITION v2

- **Levier distinctif :** La peur de manquer de loyer devient plus forte que l'indignation devant une décision salariale.
- **Prix immédiat :** Une sortie d'emploi reportée protège et emprisonne à la fois.
- **Écho à construire :** Le besoin d'études du chapitre 5 devient plus coûteux à cause de ce report.
- **Question à préserver :** Le salaire limité résulte-t-il ici d'une intention ou de contraintes? Montrer les deux.

---

## Fichier : `chapter_briefs/05_l_echelle_payante.md`

# Chapitre 5 — L’échelle payante

**Statut : PROPOSITION**, non canon narratif.

## Partie / focalisation

Partie 1. **Entités :** Envie / Prudence.

## Situation initiale

Deux candidates également capables disposent de temps, d’argent et de réseaux très différents pour se former.

## Chaîne de nécessité

Emploi à temps plein → sommeil manquant → entretien moins convaincant → résultat inégal.

## Deux lectures superposées

Barrières matérielles / légère amplification d’un sentiment de honte.

## Travail du chapitre

Questionner l’idée de mérite pur, sans nier les trajectoires de mobilité.

## Risque / contrepoids

Bourses et prêts ne sont pas limités par principe à une élite minuscule : faits à vérifier selon juridiction.

## Écriture

Entrer au moment de la bascule. Aucune mise en scène décorative. Une émotion précise, un relais crédible, un effet humain visible. **Les entités se parlent entre elles, pas aux humains.**

## Sortie cherchée

Le lecteur comprend une **conséquence**, mais ne reçoit ni morale définitive ni certitude que l'entité a prévu toute la chaîne.

## Spécificité dramatique — PROPOSITION v2

- **Levier distinctif :** Un conseiller ressent une confiance spontanée envers un candidat issu de son propre réseau.
- **Prix immédiat :** Une admission, un stage ou une occasion discrète va vers quelqu'un déjà appuyé.
- **Écho à construire :** Le bénéficiaire reparaît au chapitre 10 comme relais, sans être réduit à un imposteur.
- **Question à préserver :** Quels dispositifs d'aide existent et qui peut réellement y accéder?

---

## Fichier : `chapter_briefs/06_la_protection_a_guichets.md`

# Chapitre 6 — La protection à guichets

**Statut : PROPOSITION**, non canon narratif.

## Partie / focalisation

Partie 1. **Entités :** Rupture / Justice.

## Situation initiale

Une règle utile protège des victimes mais exclut indirectement un petit acteur qui ne peut payer la conformité.

## Chaîne de nécessité

Incident initial → norme → coûts → fermeture → concentration.

## Deux lectures superposées

Compromis réglementaire / victoire partagée et contradictoire des deux camps.

## Travail du chapitre

Mettre une victime sauvée et une entreprise étouffée dans le même chapitre.

## Risque / contrepoids

Éviter toute conclusion générale « moins de règles = mieux ».

## Écriture

Entrer au moment de la bascule. Aucune mise en scène décorative. Une émotion précise, un relais crédible, un effet humain visible. **Les entités se parlent entre elles, pas aux humains.**

## Sortie cherchée

Le lecteur comprend une **conséquence**, mais ne reçoit ni morale définitive ni certitude que l'entité a prévu toute la chaîne.

## Spécificité dramatique — PROPOSITION v2

- **Levier distinctif :** Justice soutient une règle de protection; Avarice vise ensuite le prêteur d'une petite entreprise.
- **Prix immédiat :** La règle réduit un risque réel et favorise indirectement des acteurs mieux équipés.
- **Écho à construire :** La concentration d'actifs devient la matière du chapitre 13.
- **Question à préserver :** Quel dommage la règle a-t-elle effectivement évité?

---

## Fichier : `chapter_briefs/07_la_fidelite_ou_la_force.md`

# Chapitre 7 — La fidélité ou la force

**Statut : PROPOSITION**, non canon narratif.

## Partie / focalisation

Partie 2. **Entités :** Emprise / Fidélité.

## Situation initiale

Un pouvoir invoque la préservation d’une culture pour défendre une mesure contraignante.

## Chaîne de nécessité

Crainte de disparition → désir de cohésion → restriction → résistance.

## Deux lectures superposées

Débat sur les traditions / reprise démoniaque du souci angélique de transmission.

## Travail du chapitre

Distinguer patrimoine vivant, liberté de conscience et coercition.

## Risque / contrepoids

Si inspiré d’un pays contemporain : dater et vérifier le cadre réel; ne pas blanchir l’usage de la force.

## Écriture

Entrer au moment de la bascule. Aucune mise en scène décorative. Une émotion précise, un relais crédible, un effet humain visible. **Les entités se parlent entre elles, pas aux humains.**

## Sortie cherchée

Le lecteur comprend une **conséquence**, mais ne reçoit ni morale définitive ni certitude que l'entité a prévu toute la chaîne.

## Spécificité dramatique — PROPOSITION v2

- **Levier distinctif :** Fidélité fait éprouver la perte d'un héritage; Emprise exploite le passage de la protection à la contrainte.
- **Prix immédiat :** Un geste public transforme un symbole culturel en obligation.
- **Écho à construire :** Le chapitre 8 peut interroger le même glissement de la protection vers le contrôle.
- **Question à préserver :** Ne pas confondre respect des traditions et oppression d'autrui.

---

## Fichier : `chapter_briefs/08_la_paix_surveillee.md`

# Chapitre 8 — La paix surveillée

**Statut : PROPOSITION**, non canon narratif.

## Partie / focalisation

Partie 2. **Entités :** Peur / Vigilance.

## Situation initiale

Une mesure de sécurité empêche certains dommages et crée de nouvelles restrictions durables.

## Chaîne de nécessité

Menace perçue → adhésion à surveillance → normalisation → nouveaux abus possibles.

## Deux lectures superposées

Arbitrage sécurité/libertés / contagion des émotions.

## Travail du chapitre

Montrer qui est réellement protégé et qui perd la possibilité de contester.

## Risque / contrepoids

Ne pas assimiler une mesure de prévention à une dictature sans preuves.

## Écriture

Entrer au moment de la bascule. Aucune mise en scène décorative. Une émotion précise, un relais crédible, un effet humain visible. **Les entités se parlent entre elles, pas aux humains.**

## Sortie cherchée

Le lecteur comprend une **conséquence**, mais ne reçoit ni morale définitive ni certitude que l'entité a prévu toute la chaîne.

## Spécificité dramatique — PROPOSITION v2

- **Levier distinctif :** Vigilance nourrit le sentiment de sécurité que promet une mesure; Peur rend l'alternative intolérable.
- **Prix immédiat :** Des habitants gagnent une protection tout en perdant une possibilité d'expression.
- **Écho à construire :** Une conséquence médiatique peut réapparaître au chapitre 11.
- **Question à préserver :** Fonder tout jugement sur des effets situés, non sur l'étiquette « sécurité ».

---

## Fichier : `chapter_briefs/09_le_prix_paye_par_d_autres.md`

# Chapitre 9 — Le prix payé par d’autres

**Statut : PROPOSITION**, non canon narratif.

## Partie / focalisation

Partie 2. **Entités :** Orgueil / Courage.

## Situation initiale

Deux camps ennemis présentent chacun leurs actes comme nécessaires pour protéger les leurs.

## Chaîne de nécessité

Deuil public → refus de recul → mobilisation → coût humain → récits concurrents.

## Deux lectures superposées

Conflit, défense, conscription / manipulation émotionnelle fictive.

## Travail du chapitre

Une même entité peut convoiter les deux côtés sans égalité automatique de responsabilité.

## Risque / contrepoids

Si appui sur Ukraine/Russie ou autre guerre, respecter chronologie, droit international et sources opposables.

## Écriture

Entrer au moment de la bascule. Aucune mise en scène décorative. Une émotion précise, un relais crédible, un effet humain visible. **Les entités se parlent entre elles, pas aux humains.**

## Sortie cherchée

Le lecteur comprend une **conséquence**, mais ne reçoit ni morale définitive ni certitude que l'entité a prévu toute la chaîne.

## Spécificité dramatique — PROPOSITION v2

- **Levier distinctif :** Une émotion de fermeté circule entre cabinet, conseiller et porte-parole sans être implantée chez le chef d'État.
- **Prix immédiat :** Une décision militaire ou de mobilisation impose des coûts que la scène garde visibles.
- **Écho à construire :** Le chapitre 16 révèle que les entités ont pu mal prévoir l'effet d'un relais.
- **Question à préserver :** Si cas réel, vérifier date, responsabilité, sources et distinguer défense et agression.

---

## Fichier : `chapter_briefs/10_la_porte_deja_ouverte.md`

# Chapitre 10 — La porte déjà ouverte

**Statut : PROPOSITION**, non canon narratif.

## Partie / focalisation

Partie 2. **Entités :** Avarice / Concorde.

## Situation initiale

Une nomination paraît fondée sur la compétence mais dépend aussi d’une rencontre inaccessible aux autres.

## Chaîne de nécessité

Invitation privée → familiarité → recommandation → poste → nouvelle faveur.

## Deux lectures superposées

Capital social / gestion d’affects dans le réseau.

## Travail du chapitre

Montrer la transmission douce des avantages, sans exposé sur une caste secrète.

## Risque / contrepoids

Ne pas accuser une personne nommée de favoritisme sans preuve précise.

## Écriture

Entrer au moment de la bascule. Aucune mise en scène décorative. Une émotion précise, un relais crédible, un effet humain visible. **Les entités se parlent entre elles, pas aux humains.**

## Sortie cherchée

Le lecteur comprend une **conséquence**, mais ne reçoit ni morale définitive ni certitude que l'entité a prévu toute la chaîne.

## Spécificité dramatique — PROPOSITION v2

- **Levier distinctif :** Emprise consolide un lien de confiance déjà ancien; Orgueil accentue le prestige du candidat recommandé.
- **Prix immédiat :** Une nomination semble normale à ceux qui partagent le réseau; elle paraît opaque aux exclus.
- **Écho à construire :** Le chapitre 13 peut montrer le pouvoir institutionnel acquis après cette nomination.
- **Question à préserver :** Une relation préexistante ne démontre pas, à elle seule, l'incompétence ou la corruption.

---

## Fichier : `chapter_briefs/11_ce_que_la_foule_a_entendu.md`

# Chapitre 11 — Ce que la foule a entendu

**Statut : PROPOSITION**, non canon narratif.

## Partie / focalisation

Partie 2. **Entités :** Envie / Justice.

## Situation initiale

Une phrase ambiguë devient un scandale avant que son contexte ait circulé.

## Chaîne de nécessité

Froissement personnel → extrait partagé → indignation relayée → décision précipitée.

## Deux lectures superposées

Dynamique médiatique / déformation accélérée par des impulsions.

## Travail du chapitre

Montrer la frontière entre information vérifiable et émotion collective.

## Risque / contrepoids

Ne pas inventer un faux scandale attaché à une personne réelle nommée.

## Écriture

Entrer au moment de la bascule. Aucune mise en scène décorative. Une émotion précise, un relais crédible, un effet humain visible. **Les entités se parlent entre elles, pas aux humains.**

## Sortie cherchée

Le lecteur comprend une **conséquence**, mais ne reçoit ni morale définitive ni certitude que l'entité a prévu toute la chaîne.

## Spécificité dramatique — PROPOSITION v2

- **Levier distinctif :** Envie saisit la blessure d'un témoin; un extrait sort avant son contexte.
- **Prix immédiat :** Une indignation publique éclate, puis persiste malgré une correction.
- **Écho à construire :** Le chapitre 14 peut transformer cette réaction en mesure formelle.
- **Question à préserver :** L'erreur d'information doit être inventée ou documentée avant toute attribution réelle.

---

## Fichier : `chapter_briefs/12_le_brevet_de_l_impossible.md`

# Chapitre 12 — Le brevet de l’impossible

**Statut : PROPOSITION**, non canon narratif.

## Partie / focalisation

Partie 2. **Entités :** Rupture / Prudence.

## Situation initiale

Un inventeur défie une interdiction; la découverte libère certains et expose d’autres à un risque.

## Chaîne de nécessité

Frustration → divulgation → adoption → bénéfice → usage dangereux.

## Deux lectures superposées

Innovation et précaution / stratégie des deux camps.

## Travail du chapitre

La même action garde deux conséquences incompatibles.

## Risque / contrepoids

Éviter la magie technologique et toute instruction dangereuse; préférer les impacts humains.

## Écriture

Entrer au moment de la bascule. Aucune mise en scène décorative. Une émotion précise, un relais crédible, un effet humain visible. **Les entités se parlent entre elles, pas aux humains.**

## Sortie cherchée

Le lecteur comprend une **conséquence**, mais ne reçoit ni morale définitive ni certitude que l'entité a prévu toute la chaîne.

## Spécificité dramatique — PROPOSITION v2

- **Levier distinctif :** Rupture donne à un scientifique le soulagement de partager une découverte; Prudence réveille la crainte d'un usage nocif.
- **Prix immédiat :** La diffusion ouvre un bien possible et un dommage possible.
- **Écho à construire :** Le chapitre 15 peut montrer un bénéfice imprévu plutôt qu'une justification automatique.
- **Question à préserver :** Quelle technologie imaginaire peut servir la scène sans inventer un risque concret de sécurité?

---

## Fichier : `chapter_briefs/13_la_querelle_des_vainqueurs.md`

# Chapitre 13 — La querelle des vainqueurs

**Statut : PROPOSITION**, non canon narratif.

## Partie / focalisation

Partie 3. **Entités :** Rupture / Avarice / Lucifer.

## Situation initiale

Une crise réussit à enrichir Avarice mais referme les possibilités que Rupture voulait ouvrir.

## Chaîne de nécessité

Dérégulation → consolidation du plus fort → nouvelle dépendance.

## Deux lectures superposées

Cycles de marché plausibles / dispute des fins démoniaques.

## Travail du chapitre

Les protagonistes acquièrent de la profondeur par leurs conflits sans conversion.

## Risque / contrepoids

Ne pas substituer une doctrine simpliste à la pluralité des résultats possibles.

## Écriture

Entrer au moment de la bascule. Aucune mise en scène décorative. Une émotion précise, un relais crédible, un effet humain visible. **Les entités se parlent entre elles, pas aux humains.**

## Sortie cherchée

Le lecteur comprend une **conséquence**, mais ne reçoit ni morale définitive ni certitude que l'entité a prévu toute la chaîne.

## Spécificité dramatique — PROPOSITION v2

- **Levier distinctif :** Avarice tente de conserver une infrastructure dont Rupture veut briser la domination.
- **Prix immédiat :** Les démons s'opposent tactiquement; les bénéficiaires humains changent selon l'issue.
- **Écho à construire :** Leurs opérations incompatibles précipitent l'erreur du chapitre 16.
- **Question à préserver :** Les deux demeurent des démons, sans changement de loyauté.

---

## Fichier : `chapter_briefs/14_le_mal_d_une_bonne_regle.md`

# Chapitre 14 — Le mal d’une bonne règle

**Statut : PROPOSITION**, non canon narratif.

## Partie / focalisation

Partie 3. **Entités :** Justice / Indifférence.

## Situation initiale

Une organisation prévient une injustice visible mais déplace une souffrance moins visible.

## Chaîne de nécessité

Règlement → protection mesurable → coût caché → exclusion.

## Deux lectures superposées

Arbitrage institutionnel / aveuglement céleste.

## Travail du chapitre

Forcer l’ange à défendre rationnellement son résultat sans en connaître tous les coûts.

## Risque / contrepoids

La souffrance évitée doit être aussi concrète que la souffrance produite.

## Écriture

Entrer au moment de la bascule. Aucune mise en scène décorative. Une émotion précise, un relais crédible, un effet humain visible. **Les entités se parlent entre elles, pas aux humains.**

## Sortie cherchée

Le lecteur comprend une **conséquence**, mais ne reçoit ni morale définitive ni certitude que l'entité a prévu toute la chaîne.

## Spécificité dramatique — PROPOSITION v2

- **Levier distinctif :** Une plainte légitime a provoqué une règle; des exemptions complexes en éliminent les plus petits acteurs.
- **Prix immédiat :** Une protection s'améliore, mais une concentration économique s'accélère.
- **Écho à construire :** Reprendre les coûts au chapitre 17 pour interroger la conception angélique de la venue.
- **Question à préserver :** Ne pas écrire que protéger est toujours oppressif.

---

## Fichier : `chapter_briefs/15_le_bien_de_la_rupture.md`

# Chapitre 15 — Le bien de la rupture

**Statut : PROPOSITION**, non canon narratif.

## Partie / focalisation

Partie 3. **Entités :** Rupture / Concorde.

## Situation initiale

Une institution dysfonctionnelle est renversée; sa chute crée la possibilité d’une vie plus digne et une période de précarité.

## Chaîne de nécessité

Indignation → geste qui rompt → instabilité → initiative commune.

## Deux lectures superposées

Mobilisation sociale / initiative démoniaque paradoxalement bénéfique.

## Travail du chapitre

Ne pas assimiler toute destruction au progrès; montrer les personnes exposées.

## Risque / contrepoids

Éviter d’idéaliser une révolte fictive pour justifier des violences réelles.

## Écriture

Entrer au moment de la bascule. Aucune mise en scène décorative. Une émotion précise, un relais crédible, un effet humain visible. **Les entités se parlent entre elles, pas aux humains.**

## Sortie cherchée

Le lecteur comprend une **conséquence**, mais ne reçoit ni morale définitive ni certitude que l'entité a prévu toute la chaîne.

## Spécificité dramatique — PROPOSITION v2

- **Levier distinctif :** Rupture pousse un salarié à rompre un silence; des alliés se regroupent sans que cela ait été prévu.
- **Prix immédiat :** L'acte initial fait aussi du mal à des personnes dépendantes de l'institution.
- **Écho à construire :** Un bénéficiaire du chapitre 18 peut devoir choisir s'il pardonne l'instigateur.
- **Question à préserver :** Un effet favorable ne blanchit pas toutes les conséquences de la méthode.

---

## Fichier : `chapter_briefs/16_l_erreur_de_calcul.md`

# Chapitre 16 — L’erreur de calcul

**Statut : PROPOSITION**, non canon narratif.

## Partie / focalisation

Partie 3. **Entités :** Peur / Compassion.

## Situation initiale

Un geste censé prévenir une tragédie en déclenche une autre par effet de relais.

## Chaîne de nécessité

Intuition salvatrice → freinage → collision secondaire → dilemme de responsabilité.

## Deux lectures superposées

Complexité du réel / limites des prévisions célestes.

## Travail du chapitre

Les entités ne peuvent se prévaloir d’une connaissance totale des conséquences.

## Risque / contrepoids

La surprise ne doit pas devenir un artifice; semer le coût possible tôt.

## Écriture

Entrer au moment de la bascule. Aucune mise en scène décorative. Une émotion précise, un relais crédible, un effet humain visible. **Les entités se parlent entre elles, pas aux humains.**

## Sortie cherchée

Le lecteur comprend une **conséquence**, mais ne reçoit ni morale définitive ni certitude que l'entité a prévu toute la chaîne.

## Spécificité dramatique — PROPOSITION v2

- **Levier distinctif :** Peur influence le bon relais au mauvais moment; une personne agit autrement que prévu.
- **Prix immédiat :** Les entités revendiquent ou contestent une conséquence qu'elles maîtrisent mal.
- **Écho à construire :** Cette erreur nourrit la dispute doctrinale du chapitre 17.
- **Question à préserver :** Ne pas fixer à la dernière minute une règle magique qui annulerait les limites déjà établies.

---

## Fichier : `chapter_briefs/17_la_venue.md`

# Chapitre 17 — La venue

**Statut : PROPOSITION**, non canon narratif.

## Partie / focalisation

Partie 3. **Entités :** Lucifer / Rupture / Prudence.

## Situation initiale

Les entités débattent de ce que leurs victoires ont réellement préparé.

## Chaîne de nécessité

Accumulation de « succès » contradictoires → doute sur le critère de victoire.

## Deux lectures superposées

Histoire sociale / crise des interprétations angéliques et démoniaques.

## Travail du chapitre

Faire entendre des conceptions métaphysiques rivales sans exposition interminable.

## Risque / contrepoids

L’apparition de Dieu est ouverte; pas de changement de camp imposé.

## Écriture

Entrer au moment de la bascule. Aucune mise en scène décorative. Une émotion précise, un relais crédible, un effet humain visible. **Les entités se parlent entre elles, pas aux humains.**

## Sortie cherchée

Le lecteur comprend une **conséquence**, mais ne reçoit ni morale définitive ni certitude que l'entité a prévu toute la chaîne.

## Spécificité dramatique — PROPOSITION v2

- **Levier distinctif :** Lucifer et les autres démons doivent interpréter une issue qu'aucun n'arrive à s'approprier.
- **Prix immédiat :** Un débat sur la manifestation de Dieu prend appui sur des conséquences humaines, pas sur une révélation qui résout tout.
- **Écho à construire :** Le chapitre 18 répond par un acte concret plutôt que par une doctrine.
- **Question à préserver :** La présence finale de Dieu n'est pas canonisée.

---

## Fichier : `chapter_briefs/18_les_mains_qui_choisissent.md`

# Chapitre 18 — Les mains qui choisissent

**Statut : PROPOSITION**, non canon narratif.

## Partie / focalisation

Partie 3. **Entités :** Ensemble démoniaque, présence angélique.

## Situation initiale

Un geste humain a une valeur et des conséquences que les entités ne savent pas classer.

## Chaîne de nécessité

Série d’influences modestes → choix humain incomplet → conséquence apaisante mais ambiguë.

## Deux lectures superposées

Décision autonome selon le témoin / destin préparé selon les entités.

## Travail du chapitre

Terminer le récit sur compréhension et vertige, non sur une démonstration définitive.

## Risque / contrepoids

Ne pas mentionner King Klown dans la narration; la note finale reste hors récit.

## Écriture

Entrer au moment de la bascule. Aucune mise en scène décorative. Une émotion précise, un relais crédible, un effet humain visible. **Les entités se parlent entre elles, pas aux humains.**

## Sortie cherchée

Le lecteur comprend une **conséquence**, mais ne reçoit ni morale définitive ni certitude que l'entité a prévu toute la chaîne.

## Spécificité dramatique — PROPOSITION v2

- **Levier distinctif :** Un humain prend une décision que plusieurs entités ont préparée sans qu'aucune puisse la réclamer entièrement.
- **Prix immédiat :** Le dommage demeure, une réparation partielle devient possible, la certitude morale baisse.
- **Écho à construire :** La note King Klown suit **hors récit**, sans anticipation explicative.
- **Question à préserver :** L'apaisement ne doit pas devenir absence de justice ni absolution universelle.

---

# Documentation et sources

## Fichier : `reference/AUTHOR_ESSAYS_SYNTHESIS.md`

# Synthèse de lecture des deux textes de l'auteur

## 2015 — *Déterminisme divin*

Hypothèse soutenue : la culture moderne peut surestimer l'indépendance de la volonté vis-à-vis de Dieu. L'essai contraste des conceptions anciennes du divin et des affirmations modernes de liberté; il examine inspiration, art, intuition, réactions décisives et responsabilité. **Il ne prétend pas pouvoir prouver avec certitude le contrôle divin.**

### Conséquences utiles pour la fiction

- Une décision peut être modifiée sans voix surnaturelle ni miracle perceptible.
- L'inspiration est une piste philosophique et une source d'imagerie narrative.
- Le débat responsabilité / pardon peut fournir la paix finale, sans faire disparaître les victimes ou les faits.

## 2026 — *The Human Being as a Prompted Creature*

Idée pivot : l'humain ne produit pas ses pensées ex nihilo; il répond à des sollicitations biologiques, sociales, émotionnelles et culturelles. Le texte recourt à une analogie de **prompt**, et insiste sur les instants où un oui, un lapsus ou un appel change une vie. Le moi construit ensuite une narration de ce qu'il considère avoir choisi.

### Conséquences utiles pour la fiction

- Donner à chaque scène un **prompt ressenti** : envie, honte, urgence, paix, peur.
- Relier plusieurs personnes : A est « prompté » puis influence B par une action ordinaire.
- Rendre le lecteur lucide plutôt que fataliste : la vigilance sur les influences est une forme de discernement.

## Tension féconde

L'essai de 2015 doute de la liberté souveraine; le texte de 2026 redéfinit la liberté comme discernement. Le roman peut explorer la tension **sans trancher l'ontologie du monde réel**.

## Éthique d'adaptation

Les deux textes sont une **base intellectuelle fournie par l'auteur**. Les interventions célestes sont un dispositif imaginaire. Ne pas présenter les émotions, lapsus ou symptômes dans la vie réelle comme des preuves de possession.

---

## Fichier : `reference/CASE_FILE_TEMPLATE.md`

# DOSSIER-CAS — MODÈLE À COPIER, PAS UN CAS VÉRIFIÉ

**ID** : CAS-XXX  
**Chapitre(s)** : À déterminer  
**Événement / enjeu** :  
**Lieu / période** :  
**Statut** : À DOCUMENTER

## 1. Chronologie des faits publics

| Date | Fait précis | Source primaire ou indépendante | Consultée le | Niveau de confiance |
|---|---|---|---|---|
| À compléter | | | | |

## 2. Énoncés controversés et positions

| Énoncé | Qui le soutient? | Preuves à l'appui | Limites / contradictions |
|---|---|---|---|
| | | | |

## 3. Explication humaine suffisante

Contraintes, intérêts, institutions, délais, émotions ordinaires. Ce paragraphe doit fonctionner **sans aucune entité céleste**.

## 4. Extrapolation FICTION

Quel personnage composite, dialogue privé ou resserrement narratif est inventé? Ne rien laisser ambigu dans le dossier interne.

## 5. Chaîne céleste FICTION

`Émotion chez A → action A → signal reçu par B → interprétation B → conséquence C`

## 6. Contrefactuel et coût

- Sans l'influence, que se produirait-il probablement?
- Qui gagne? Qui perd, y compris indirectement?
- Qui demeure responsable sur le plan institutionnel dans le récit?

## 7. Contrôle final

- [ ] Faits datés, sources fiables, interprétations attribuées
- [ ] Aucune citation privée inventée présentée comme authentique
- [ ] Cause ordinaire intelligible
- [ ] Aucune allégation de possession réelle
- [ ] Seconde lecture dramaturgique utile

---

## Fichier : `reference/CASE_STUDY_PROTOCOL.md`

# Protocole de cas — réalisme documentaire, fantastique assumé

Le but est de rendre le monde **exact**, non de présenter une entité fictive comme un acteur politique établi.

## Séparer cinq couches

1. **Fait public** : date, institution, acte, décision, citation courte d'une source identifiée.
2. **Contexte établi** : textes applicables, contraintes économiques, conséquences documentées.
3. **Désaccord réel** : interprétations concurrentes attribuées à leurs auteurs ou à leurs études.
4. **Extrapolation littéraire** : scènes privées, choix d'un composite, resserrement chronologique identifié.
5. **Couche céleste** : intervention entièrement fictionnelle par émotion, relais ou lapsus.

## Minimum pour écrire une scène historique

- chronologie de 3 à 8 jalons sourcés;
- deux sources indépendantes quand le sujet est contesté;
- une explication humaine robuste, même si la couche fantastique disparaît;
- une conséquence pour des personnes autres que le dirigeant;
- un point de friction moral : ce que l'autre interprétation protège ou explique;
- une note `FICTION` dans les documents internes pour tout geste/pensée inventé.

## Drapeaux de révision

- Toute citation attribuée à un vivant sans source primaire.
- Tout événement dont les dates ont été fusionnées pour la fluidité.
- Une responsabilité juridique ou historique déduite d'une simple intention prêtée.
- Des scènes d'influence céleste utilisées comme preuve d'un conflit d'intérêts réel.
- Une image « officielle » ou un chapitre qui ferait croire à un dossier d'enquête authentique plutôt qu'à une fiction.

## Vérification juridique et éditoriale

Le pseudonyme Colin Row est un choix de publication; il ne constitue pas une garantie d'anonymat. Pour les personnages publics vivants, faire relire les passages factuellement sensibles par une personne compétente avant publication. Éviter les accusations inventées (crime, corruption, abus) présentées hors fiction comme des faits.

---

## Fichier : `reference/EXAMPLE_CASE_FILE_FICTION.md`

# CAS-TEST-01 — réforme reportée (ENTIÈREMENT FICTIF)

Ce dossier sert de **référence de méthode**, pas de preuve ou de reportage.

## 1. Faits publics

Aucun. Pays, ministre, entreprise et réforme non identifiés. Toutes les personnes et décisions sont fictives.

## 2. Explication ordinaire

Un projet réglementaire provoque des craintes chez une entreprise. Son dirigeant contacte un élu; l'élu saisit le cabinet compétent; le responsable reporte une signature pour examiner les risques. Tous ont des motivations humaines plausibles.

## 3. Couche céleste

Avarice amplifie la peur de perdre chez le dirigeant d'entreprise. Orgueil augmente le sentiment d'importance de l'élu. Aucun démon n'a besoin d'approcher le ministre.

## 4. Contrefactuel

Sans amplification, le dirigeant aurait probablement attendu; le message serait arrivé après la signature. La décision aurait donc suivi une autre procédure, pas nécessairement une autre issue finale.

## 5. Ambivalence morale

Le report peut éviter des coûts inutiles ou laisser perdurer une injustice. La scène ne doit pas imposer la réponse par son vocabulaire.

## 6. Ce qui demeure ouvert

Effet à long terme, état du projet après le report, coût humain documenté **dans le monde du roman**. À connecter à un chapitre ultérieur si retenu.

---

## Fichier : `reference/FACT_CHECK_LEDGER.md`

# Registre des faits à vérifier — non consultés dans ce dépôt

**ATTENTION :** ce registre n'atteste aucun fait récent. Il désigne seulement ce qui exigerait des sources datées avant rédaction finale.

| ID | Chapitre(s) | Domaine / question | Statut | Preuve attendue |
|---|---|---|---|---|
| F-01 | 4 | Pouvoir de négociation, précarité, bas salaires au Canada/Québec | À VÉRIFIER | Statistiques et études récentes, période et population |
| F-02 | 5 | Accès postsecondaire par revenu; aide financière accessible au Québec | À VÉRIFIER | Données de cohorte, règles officielles |
| F-03 | 6,14 | Exemples de réglementation à bénéfice et coût démontrables | À VÉRIFIER | Textes de loi + études d'impact |
| F-04 | 7 | Lois ou mesures relatives aux traditions/cultures et droits | À VÉRIFIER | Sources officielles, droits applicables |
| F-05 | 8 | Mesures de sécurité et effets documentés sur droits civils | À VÉRIFIER | Décisions, rapports indépendants |
| F-06 | 9 | Dates, séquences, responsabilité, mobilisation dans un conflit donné | À VÉRIFIER | Sources primaires + recoupement |
| F-07 | 10 | Réseaux de nomination et déterminants de l'accès aux postes | À VÉRIFIER | Études empiriques, dossiers précis |
| F-08 | 11 | Un cas vérifié de débat médiatique et de correction | À VÉRIFIER | Enregistrements, chronologie |
| F-09 | 12 | Cas d'innovation, interdiction, externalités | À VÉRIFIER | Documents techniques/juridiques |
| F-10 | 4,10 | Gouvernance et rémunération des dirigeants de coopératives | À VÉRIFIER | Rapports annuels et politique de rémunération |

Ajouter colonnes `source`, `date de consultation`, `citation` et `statut de vérification` au moment de la recherche. **L'absence de preuve doit rester visible.**

---

## Fichier : `reference/INFLUENCE_VS_EVIDENCE.md`

# Causalité visible / interprétation invisible

Le roman a deux plans. Le plan humain possède des explications ordinaires (histoire, intérêts, institutions, psychologie). Le plan céleste constitue l'interprétation **fantastique** que la fiction donne au lecteur. On n'utilise pas le manque de preuve d'une cause humaine comme preuve d'un démon.

## Test d'un cas

1. Le fait public a-t-il une source vérifiable et une date?
2. L'explication humaine est-elle suffisante pour rendre l'événement plausible sans magie?
3. La décision imputée à une personne réelle est-elle son acte public, non une pensée inventée donnée comme vérité?
4. L'intervention démoniaque ou angélique modifie-t-elle le **ressenti d'une personne spécifique**, plutôt que « l'Histoire » de manière vague?
5. Si l'entité se trompe, la scène reste-t-elle intéressante?
6. Le lecteur peut-il recevoir l'idée philosophique sans être invité à soupçonner des personnes réelles d'une possession authentique?

## Fonction de l'ambiguïté

**Crédibilité littéraire ≠ prétention documentaire sur le surnaturel.** La mise en abyme finale élargit la fiction; elle ne transforme pas le roman en témoignage vérifié.

---

## Fichier : `reference/PHILOSOPHICAL_ANCHORS.md`

# Appuis philosophiques — lectures de l'auteur, non preuves du surnaturel

**Texte de 2015 — `Determinisme_divin_v14.md`** : hypothèse que l'inspiration divine peut infléchir le choix; contrastes historiques entre croyances de l'intervention et idéal moderne d'autonomie; importance du débat théologique sur la liberté; responsabilité et pardon. L'auteur lui-même reconnaît dans sa conclusion l'absence de certitude sur la question. Voir la source pour les citations et limites.

**Texte de 2026 — `The_Human_Being_as_a_Prompted_Creature_2026.txt`** : l'humain répond à des sollicitations physiques, affectives, sociales ou spirituelles; l'ego attribue après coup à son « je » ce qui a été déclenché ailleurs; la liberté pourrait être un discernement des influences plutôt que leur absence.

## Transposition dans le roman

| Question d'essai | Traduction dramatique possible |
|---|---|
| D'où vient l'inspiration? | un acte de création naît d'un ressenti qu'aucun protagoniste humain ne peut situer |
| Qu'est-ce qu'une volonté? | plusieurs options existent jusqu'à ce qu'une émotion change leur poids |
| Qui est l'auteur de la décision? | un humain agit, puis trois entités revendiquent des maillons différents |
| Que vaut la culpabilité? | un dommage existe même lorsque l'intention n'a pas été souveraine |
| Peut-on discerner l'influence? | la personne reconnaît ses propres habitudes et retarde un réflexe, sans démonstration surnaturelle |

## Discipline d'argumentation

La philosophie sert à fabriquer un **problème visible**, pas à plaider que des démons expliquent réellement un lapsus. Des avancées en psychologie ou neurosciences ne démontreraient pas automatiquement le surnaturel; inversement, une zone d'ignorance scientifique n'en constitue pas une preuve.

---

## Fichier : `reference/REAL_PEOPLE_AND_HISTORY.md`

# Personnes réelles et événements publics

## Règle de base

Les personnages centraux sont les **êtres fictifs**. Un dirigeant réel, si son nom apparaît, sert de carrefour d'enjeux publics vérifiables, **pas** de preuve qu'une force occulte le contrôle réellement.

## Casting possible, non fixé (recherche préalable requise)

- Donald Trump : pouvoir personnel, rapport à la réputation, négociation.
- Vladimir Poutine : tradition, sécurité, frontières entre protection revendiquée et coercition.
- Volodymyr Zelensky : défense, mobilisation, coût humain, conditions d'une négociation.
- Benjamin Netanyahu : sécurité, mesures militaires, protection de civils et conséquences.
- Mark Carney : gouvernance économique, responsabilité publique, prévention des conflits d'intérêts.
- Xi Jinping : continuité institutionnelle, ordre collectif, contrôle politique.
- Dirigeants de grandes institutions financières ou coopératives : rémunération, gouvernance, réseaux, rapport au service.

Ces lignes **ne sont pas des allégations de motivations privées**. Ce sont des thèmes de recherche ou de construction de personnages composites.

## Faits / interprétations / fiction

Pour chaque scène :

| Couche | Exemple de formulation dans une fiche |
|---|---|
| **Fait attesté** | Un discours daté, une loi identifiée, une décision publiée |
| **Interprétation** | La mesure favorise telle valeur au détriment de telle autre — débat ouvert |
| **Fiction** | Peur influence un conseiller qui transmet une inquiétude à un cabinet |

## Cas contemporains contestés

Sur la guerre en Ukraine, séparer impérativement les faits d'invasion et de responsabilité internationale, les décisions de mobilisation, les discussions sur neutralité et les débats de droits linguistiques. Aucun élément isolé ne doit se transformer en justification automatique d'une agression ni en immunité contre la critique. Même méthode pour Gaza/Israël, régulations et affaires financières.

## Publication

Le pseudonyme ne garantit pas l'anonymat légal. Avant publication d'une fiction utilisant des personnalités vivantes : révision juridique et factuelle compétente, juridiction de publication à préciser. Ne pas introduire de fausses citations ou d'accusations spécifiques inédites.

---

## Fichier : `reference/REPO_MODEL_ALIGNMENT.md`

# Alignement avec le dépôt modèle `Colin_Row.zip`

## Éléments repris comme méthode de travail

| Dépôt modèle | Présent dépôt | Adaptation |
|---|---|---|
| `core/00_CANONICAL_STATE.md` | idem | séparer clairement les décisions auteur du plan hypothétique |
| `core/01_BOOK_BIBLE.md` | idem | roman philosophique des influences, pas roman carcéral |
| `core/02_EDITORIAL_CONTRACT.md` | idem | critère de crédibilité et prudence sur figures réelles |
| `core/03_VOICE_AND_STYLE.md` | idem | densité extrême, ressenti, zéro décor non causal |
| `core/04_CHARACTER_BIBLE.md` | idem | entités célestes; figures humaines limitées aux fonctions publiques |
| `core/05_THEMES_MOTIFS.md` | idem | appels, lapsus, chaînes, récit de l'ego |
| `core/06_CONTINUITY_MAP.md` | idem | lois fictionnelles + scènes compatibles |
| `core/07_AMBIGUITIES_AND_DECISIONS.md` | idem | décisions ouvertes réellement ouvertes |
| `core/08_WRITING_PROTOCOL.md` | idem | protocole de production/révision de scène |
| `core/09_CHAINES_DE_NECESSITE.md` | `core/09_CHAINES_DE_CAUSALITE.md` | relais émotionnels au lieu de genèse de modules |
| `core/10_CHAPTER_ENGINE.md` | idem | cinq fils narratifs par chapitre |
| `core/11_CANON_DECISIONS_V3.md` | `core/11_CANON_DECISIONS_V1.md` | première version propre au projet |
| `parts/` | idem | trois mouvements hypothétiques |
| `chapter_briefs/` | idem | 18 briefs provisoires, pas copie des 19 |
| `reference/`, `material/`, `manuscript/`, `working/` | idem | sources, stock non canon, roman, essais |
| `FULL_CONTENT.md`, `INDEX.md`, `REPO_MANIFEST.md` | idem | navigation et compilation reproductible |

## Non repris

Aucune intrigue de prison, aucune technologie KOA/Konnaxion, aucune biographie ou causalité du roman Colin Row. La relation entre les deux œuvres ici envisagée **n'ajoute aucun dévoilement** dans le texte du présent roman.

---

## Fichier : `reference/SOURCE_INDEX.md`

# Index des sources

## Sources de l'auteur (SOURCE, pas canon automatique)

1. `reference/sources/Determinisme_divin_v14.md` — essai du **24 avril 2015** : histoire des conceptions du libre arbitre, grâce/inspiration, responsabilité, hypothèse d'une influence de Dieu. Document source fourni par l'auteur.
2. `reference/sources/The_Human_Being_as_a_Prompted_Creature_2026.txt` — texte du **18 mai 2026** : humain comme être sollicité, réseaux d'influence, micro-bifurcations, ego narrateur, discernement. Copie du texte transmis dans la conversation; peut contenir du mobilier de page web.
3. `Colin_Row.zip` (non recopié) — **source de structure documentaire** : canon, briefs, continuité, matériaux, manuscrit, réserves et compilation. N'appartient pas à l'intrigue de ce roman.
4. **Échanges d'élaboration, octobre 2026** — décisions **CANON** de ce dépôt : personnages démoniaques, camps, influence non verbale et distribué, densité, final King Klown.

## Hiérarchie

**Décision explicite récente de l'auteur > proposition actuelle > texte-source historique > exemple improvisé.** Un ancien essai peut éclairer sans établir la physique de l'univers romanesque.

## Consigne

Quand un extrait d'essai présente une hypothèse du réel, le roman peut l'expérimenter **fictionnellement**. Ne pas transformer une thèse philosophique en fait démontré.

---

## Fichier : `reference/case_files/README.md`

# Dossiers-cas factuels — aucun cas réel vérifié pour le moment

Créer ici un fichier par événement réel **après recherche**, à partir de `../CASE_FILE_TEMPLATE.md`.

Ne jamais convertir les scènes-tests entièrement fictives en faits. Distinguer dates, sources, interprétations publiques, invention narrative et intervention céleste fictive.

---

# Atelier et intrigues

## Fichier : `working/CAUSAL_DEPENDENCY_SKETCH.md`

# Esquisse de dépendances entre chapitres (18 chapitres = PROPOSITION)

L'idée est de transformer une **anthologie de mécanismes** en **intrigue cumulative**. Ces flèches ne sont pas des décisions de l'auteur.

## Chaîne économique possible

`01 (parole qui échappe) → 04 (dépendance salariale) → 05 (études et sélection) → 10 (réseaux) → 13 (capture d'un secteur) → 14 (coût des protections)`

La parole d'une salariée modifie sa carrière; sa précarité pèse sur le choix d'études d'un proche; l'orientation du proche permet un contact, qui rend possible une future décision de gouvernance; une réglementation protège mais concentre davantage. L'influence céleste doit être une **série de petits points d'appui**, pas une prophétie exhaustive.

## Chaîne politique possible

`02 (appel) → 06 (règlement ajourné) → 08 (sécurité) → 11 (traitement public) → 16 (effet imprévu)`

Un relais d'abord banal entraîne une décision dont les conséquences donnent un nouveau rôle à une règle protectrice; un récit public amplifie ensuite la réaction; l'issue déjoue ceux qui la revendiquaient.

## Chaîne doctrinale possible

`03 (appropriation de son geste) → 07 (fidélité / emprise) → 09 (sacrifice) → 15 (bien inattendu) → 17 (divergence sur la venue) → 18 (réparation partielle)`

La même erreur de lecture de la volonté humaine, déjà présente au chapitre 3, devient de plus en plus coûteuse. Les discours célestes se raccourcissent à mesure que les conséquences pèsent.

## Test de cumul

Pour chaque flèche, inscrire plus tard : `relai = [personne, organisme, information, ressource, dette, émotion]` et **pourquoi le lecteur reconnaîtrait ce relais**. Si la relation ne résiste pas à deux phrases d'explication simple, ne pas forcer la connexion.

## Alerte

Aucune de ces séquences ne doit transformer un événement historique réel en réaction causée par un appel inventé sans avertissement littéraire clair. Les scènes publiques réelles requièrent un dossier sourcé distinct.

---

## Fichier : `working/CHANGELOG.md`

# Historique des révisions

## v2 — enrichissement éditorial et outillage

- **Conservé** : la totalité du dépôt v1, ses 18 briefs exploratoires et les deux textes-source de l'auteur.
- **Clarifié** : différence entre canon explicite, outil éditorial, proposition d'intrigue et document source.
- **Ajouté** : moteur dramatique, grammaire des influences, contradictions doctrinales, continuité causale, courbe de lecture.
- **Ajouté** : pistes d'intrigue, fils humains récurrents proposés, scènes-tests brèves, fiches de recherche, scorecard, guide de démarrage.
- **Enrichi** : briefs pour distinguer les séquences et préparer les effets différés.
- **Automatisé** : génération de `FULL_CONTENT.md`, `INDEX.md`, `REPO_MANIFEST.md` et validation structurelle.
- **Non décidé** : titre, nombre de chapitres, figure principale, apparition de Dieu et sélection de personnalités réelles.

Aucun texte du manuscrit n'a été déclaré final. Aucun cas historique controversé n'a été fact-checké dans cette livraison.

---

## Fichier : `working/DECISION_QUEUE.md`

# Décisions prioritaires sans réponse imposée

1. Le nombre de démons/anges doit-il être **exactement** sept de chaque côté?
2. Quel démon sera la focalisation principale du premier tiers?
3. Lucifer sera-t-il un personnage régulier ou un point d'origine éloigné?
4. À quelles époques se dérouleront les cas? Une période contemporaine unique ou quelques retours historiques brefs?
5. Dieu se manifeste-t-il littéralement dans l'histoire, ou reste-t-il une interprétation des deux camps?
6. Les chapitres suivront-ils 18 grandes chaînes ou une autre composition?

**Aucune de ces décisions n'est nécessaire pour comprendre le canon déjà établi.**

---

## Fichier : `working/README.md`

# Atelier — versions de travail

Tester ici : structure, chapitres, scènes, coupes, changements de voix. Lorsqu'un choix est confirmé par l'auteur, l'enregistrer dans `core/07_AMBIGUITIES_AND_DECISIONS.md` et actualiser le canon pertinent.

---

## Fichier : `working/RECURRING_HUMAN_THREADS.md`

# Relais humains récurrents — PROPOSITIONS

Le risque du plan actuel : dix-huit chapitres qui ressemblent à dix-huit exemples indépendants. Des vies récurrentes permettent de rendre visibles les coûts différés. Noms, biographies et liens ci-dessous sont purement fictifs et **non validés**.

| Fil | Situation initiale | Choix qui paraît libre | Répercussion différée |
|---|---|---|---|
| **Nora** (salariée d'une entreprise dominante) | elle n'a pas de réserve suffisante pour quitter son emploi | elle dénonce une pratique au moment où l'humiliation dépasse sa peur | pression financière, réseau de solidarité, possibilité ou perte d'emploi |
| **Malik** (étudiant et proche de Nora) | il combine études, travail et dette | il accepte / refuse une occasion exigeant du temps non rémunéré | entrée ou exclusion d'un réseau institutionnel |
| **Élise** (cadre chargée d'une règle protectrice) | ses décisions ont un coût que les tableaux ignorent | elle reporte une signature après un appel relayé | réorganisation d'un secteur, puis justification administrative |
| **Victor** (investisseur ou responsable d'organisation) | il dépend de ses partenaires et de sa réputation | il hésite entre sauver l'institution et garder le contrôle | transfert de pouvoir, changement de propriétaires |

## Deux contraintes

1. Ces personnages ne sont pas les protagonistes : **les démons le restent**. Les humains portent les effets observables, ce qui donne une mémoire aux scènes.
2. Ne pas fabriquer un hasard invraisemblable où toutes les personnes se connaissent. Une chaîne institutionnelle, économique ou médiatique peut suffire à relier leurs trajectoires.

## Pistes de reprise

- L'appel de Victor n'atteint pas directement Élise : il passe par deux intermédiaires avec leurs propres raisons d'agir.
- Une norme retardée soulage l'employeur de Nora tout en prolongeant une situation précaire.
- Nora prononce une phrase qui donne à Malik l'élan de ne pas abandonner ses études; une autre personne l'interprète comme une insulte.
- La carrière de Malik croise plus tard une décision de recrutement issue du réseau de Victor.

**Ces quatre filiations sont des outils de test; les scènes sur personnalités réelles resteraient un autre niveau de documentation et de fiction.**

---

## Fichier : `working/REVISION_BACKLOG.md`

# Carnet de révision — optimisations identifiées

## Corrigé dans la v2

- [x] Expliciter un **moteur d'intrigue** au-delà des 18 thèmes : `core/14_STORY_ENGINE.md`.
- [x] Formaliser **prise émotionnelle → relais → contrefactuel** : `core/15_GRAMMAIRE_DES_INFLUENCES.md`.
- [x] Donner à chaque entité **doctrine, méthode et contradiction** : `core/16_DOCTRINES_EN_CONFLIT.md`.
- [x] Tracer une **courbe de lecture** vers étonnement puis paix : `core/17_COURBE_DU_LECTEUR.md`.
- [x] Proposer trois intrigues concurrentes et des **fils humains récurrents**, sans les canoniser.
- [x] Ajouter des **scènes-tests contrastées**, brèves et centrées sur le ressenti.
- [x] Ajouter des **gabarits de recherche** distinguant les faits publics des fictions.
- [x] Ajouter un **contrôle automatique** de cohérence formelle et génération de l'index.

## À trancher par l'auteur quand l'écriture l'exigera

- [ ] Quelle intrigue produit la tension la plus forte sur trois scènes successives?
- [ ] Quel démon est suivi intimement au début sans devenir narrateur omniscient?
- [ ] Combien de personnages humains doivent revenir?
- [ ] Quelle durée historique permet un réalisme documentaire sans devenir chronique politique?
- [ ] Quelle dernière action produit la paix sans exposé sur la morale?
- [ ] Quel est l'équilibre entre dirigeants réels (scènes publiques vérifiées) et personnages composites?

## Ne pas corriger sans demande

Les décisions récentes de l'auteur sur les **camps immuables**, l'**influence non verbale**, les **démons protagonistes**, la **densité** et le **paragraphe final King Klown** sont le socle. Les outils n'ont pas autorité pour les modifier.

---

## Fichier : `working/SCENE_SCORECARD.md`

# Fiche d'évaluation rapide d'une scène (outil, pas verdict automatique)

> Coter chaque critère 0 (absent), 1 (fragile), 2 (solide). Une cote élevée ne remplace jamais une lecture littéraire.

| Critère | Question précise |
|---|---|
| Prise émotionnelle | Qu'est-ce qui change dans un **ressenti**, pas dans une pensée soufflée? |
| Maillon humain | Qui agit réellement, avec une raison suffisante même sans magie? |
| Bascule | Que devient différent après ce geste? |
| Coût | Qui paie? Qui gagne? À quel moment? |
| Rivalité céleste | En quoi cette scène révèle-t-elle un désaccord entre entités? |
| Superposition | Peut-on lire la scène comme un fait social et une opération surnaturelle? |
| Compression | Que peut-on retrancher sans perdre la bascule? |
| Continuité | Quel effet survit et où le reverra-t-on? |

**Signal d'alerte :** une scène notée 2 partout, mais qui répète la précédente, doit être coupée. L'originalité de la *suite* compte autant que sa qualité isolée.

**Examen de crédibilité :** si la scène utilise une personne réelle, aucune note n'est attribuée tant que les événements et citations invoqués n'ont pas été vérifiés.

---

## Fichier : `working/STORY_SPINES.md`

# Trois épines dorsales possibles — NE PAS confondre avec le canon

Le plan des dix-huit chapitres décrit pour l'instant **des thèmes**, pas une intrigue qui oblige à tourner la page. Voici trois moyens de lui donner une dynamique. Aucun n'est adopté.

## Option A — La victoire qui se retourne (structure causale)

**Protagonistes proposés** : Rupture et Avarice, antagonistes stratégiques au sein des démons.

**Question motrice** : une opération pour défaire une concentration de pouvoir peut-elle finalement accroître cette concentration?

1. Rupture déclenche une rupture locale que les humains croient fortuite.
2. Avarice récupère les ressources libérées par cette rupture.
3. Les conséquences traversent emploi, formation, dette et accès aux postes de décision.
4. Les anges restaurent la cohérence, aidant à leur insu les vainqueurs économiques.
5. Rupture doit agir contre Avarice sans cesser d'être démon; son ultime succès est impossible à classer comme victoire ou défaite.

**Force** : reprend les questions économiques initiales sans énumération. **Risque** : réduire l'univers à un seul problème de marché.

## Option B — Un événement, deux sauvetages incompatibles (structure morale)

**Question motrice** : qui a le droit de protéger un peuple, et quel prix une protection peut-elle imposer?

1. Un acte initial minime place une collectivité devant un risque réel.
2. Les anges veulent éviter la perte immédiate; les démons veulent rompre l'ordre qui a produit cette vulnérabilité.
3. Chaque camp sauve des vies dans un lieu et provoque un dommage ailleurs.
4. Les êtres célestes revendiquent des décisions prises par d'autres humains.
5. Les protagonistes constatent que la pureté de leurs fins ne dit rien de la justice de leurs moyens.

**Force** : dilemme fort. **Risque** : trop de discours théologiques sans action.

## Option C — La campagne des relais (structure d'enquête inversée)

**Question motrice** : pourquoi les plans élaborés par les démons les plus puissants échouent-ils là où un infime geste réussit?

1. Un démon est convaincu d'avoir causé une décision historique.
2. Il cherche à reproduire la méthode par plusieurs relais humains.
3. Les mêmes leviers produisent des effets contraires selon leurs contextes.
4. Un ange exploite à son tour les relais créés par le démon.
5. Le démon découvre qu'il avait mal identifié l'auteur du premier basculement.

**Force** : protagonistes célestes actifs et faillibles. **Risque** : énigme trop technique, détachée des conséquences humaines.

## Combinaison suggérée pour un test, NON DÉCIDÉE

Utiliser **A pour les conséquences**, **C pour la progression de l'enquête**, et **B pour la crise morale finale**. Écrire d'abord 3 scènes-pivots de 150–300 mots, puis évaluer quelle structure naît du texte, au lieu de verrouiller d'emblée dix-huit chapitres.

---

## Fichier : `working/variants/README.md`

# Variantes de la structure — non canon

Conserver ici des variantes écrites d'une même séquence, nommées `XX_scene_a.md`, `XX_scene_b.md`. Documenter pourquoi un montage perd ou gagne de l'effet; ne pas fusionner les variantes dans le manuscrit avant décision.

---

# Matériaux

## Fichier : `material/README.md`

# Matériaux — non canon

- `fragments/` : phrases, micro-scènes, doubles sens.
- `scenes/` : versions longues ou tests, pas validés.
- `motifs/` : pistes de répétition symbolique, à doser.
- `alternates/` : structures concurrentes ou versions incompatibles.
- `research/` : notes brutes et questions factuelles (non vérifiées tant que non sourcées).
- `legacy/` : idées d'une étape antérieure du projet, à ne pas réintroduire automatiquement.

Règle héritée de la méthode du dépôt modèle : **couper n'est pas perdre**. Un matériau intéressant n'est pas pour autant un fait canonique.

---

## Fichier : `material/alternates/README.md`

# Alternates — réserve

Espace de travail **non canonique**. Toute idée intégrée au récit doit d’abord passer par `core/07_AMBIGUITIES_AND_DECISIONS.md` et le brief concerné.

---

## Fichier : `material/fragments/01_l_appel.md`

# Fragment d'essai — L'appel (NON CANON)

Le ministre allait signer. Prudence lui avait donné, depuis trois jours, une confiance paisible dans son choix. Avarice ne chercha pas à la briser.

Il choisit un autre homme, à deux cents kilomètres de là. L'entrepreneur craignait déjà la réforme. Avarice transforma cette crainte en urgence. L'homme appela son député.

Le député voulait attendre. Orgueil lui fit sentir qu'on le prendrait enfin au sérieux. Il insista. Sa conseillère obtint une interruption de séance.

Le ministre reporta la signature.

— Tu ne l'as jamais approché, constata Prudence.

— Je n'avais pas besoin de lui, répondit Avarice.

Le lendemain, le ministre décrivit son report comme une décision de bonne gouvernance.

## Lecture de travail

- Causalité humaine : sollicitations, échéancier, arbitrage politique.
- Causalité fantastique : deux impulsions sur des personnes secondaires.
- Économie du texte : aucune couleur de meuble, aucun trajet narré, aucune voix télépathique.
- **Ne pas intégrer tel quel au manuscrit sans décision d'auteur.**

---

## Fichier : `material/legacy/README.md`

# Legacy — réserve

Espace de travail **non canonique**. Toute idée intégrée au récit doit d’abord passer par `core/07_AMBIGUITIES_AND_DECISIONS.md` et le brief concerné.

---

## Fichier : `material/motifs/LE_RELAIS.md`

# Motif en réserve — Le relais

Une décision importante appartient rarement à un seul individu. Intermédiaires, amis, employés, conseillers et étrangers apportent les signaux auxquels on répond. Le démon n'a pas besoin de diriger le roi quand il peut inquiéter son messager.

**Ne pas répéter** mécaniquement un appel par chapitre : courrier, délai, recommandation, regard, interruption, fatigue, déplacement, oubli et silence sont d'autres relais possibles.

---

## Fichier : `material/research/README.md`

# Research — réserve

Espace de travail **non canonique**. Toute idée intégrée au récit doit d’abord passer par `core/07_AMBIGUITIES_AND_DECISIONS.md` et le brief concerné.

---

## Fichier : `material/scene_tests/01_la_norme.md`

# Scène-test 01 — La norme

**NON CANON — personnages et situation fictifs.** Test d'une protection angélique aux conséquences ambivalentes.

La nouvelle norme empêcha trois accidents la première année. Justice la considéra comme une réussite.

La seconde année, plusieurs petits ateliers fermèrent. Les grandes entreprises pouvaient payer les inspections, les assurances et les avocats. Les autres non.

Avarice n'avait pas participé au vote. Il avait seulement fait naître chez un prêteur une satisfaction tranquille à l'idée d'acquérir, pour presque rien, les machines d'un atelier en faillite.

— Tu profites de ma règle, observa Justice.

— Tu me les as rendues abordables.

— Elle a sauvé des vies.

— Je n'ai pas dit le contraire.

L'ancien propriétaire cherchait désormais du travail chez celui qui avait acheté ses machines. Il était plus en sécurité qu'avant.

Il était aussi moins libre.

**Lecture visible** : bénéfices de sécurité, coûts de conformité et concentration possibles. **Lecture fantastique** : deux stratégies contradictoires trouvent avantage au même événement.

---

## Fichier : `material/scene_tests/02_le_refus.md`

# Scène-test 02 — Le refus

**NON CANON — personnages fictifs.** Test d'un bien produit par la Rupture, sans convertir le démon en héros.

On avait proposé à Léa un contrat qui renouvelait sa précarité pour une troisième année. Elle allait signer : le loyer arrivait dans six jours.

Prudence avait entretenu chez elle le soulagement de disposer au moins d'un revenu. Rupture n'essaya pas de l'effacer. Il transforma seulement une petite humiliation ancienne en sensation brusque d'étouffement.

— Non, dit Léa.

Le recruteur ne comprit pas. Léa non plus.

Le contrat fut offert à quelqu'un d'autre. Pendant dix jours, elle regretta sa réponse. Au onzième, une collègue lui proposa de joindre un recours collectif déjà en préparation.

— Elle aurait pu perdre son appartement, dit Prudence.

— Elle le peut encore, répondit Rupture.

Il n'avait pas prévu le recours. Il avait seulement voulu briser une habitude.

**Lecture visible** : refus, risque matériel, entraide non garantie. **Lecture fantastique** : un démon ouvre une possibilité sans savoir ce qu'elle contient.

---

## Fichier : `material/scene_tests/03_l_interprete.md`

# Scène-test 03 — L'interprète

**NON CANON — sommet, personnes et paroles inventés.** Test d'un relais minuscule à coût diplomatique. Ne pas attribuer à un événement historique sans dossier vérifié.

Le chef de délégation avait choisi un mot prudent. Son interprète connaissait la nuance. Au moment de parler, une honte absurde lui traversa l'esprit : il avait peur de paraître faible.

Il traduisit « difficile » par « inacceptable ».

L'autre délégation suspendit les discussions.

Orgueil observa les communiqués se durcir.

— Tu as influencé le chef? demanda Peur.

— Je n'aurais pas su trouver une ouverture aussi étroite chez lui.

L'interprète signala son erreur trop tard. Il rédigea ensuite un rapport complet pour expliquer le contresens. Plusieurs lecteurs y virent une manœuvre calculée.

Il ne savait pas ce qui l'avait pris. Orgueil, lui, savait seulement ce qu'il avait tenté, pas tout ce qu'il venait de provoquer.

**Lecture visible** : erreur, contexte de négociation, interprétation politique. **Lecture fantastique** : un affect fugace fabrique un mot irréversible.

---

## Fichier : `material/scene_tests/04_pas_de_prise.md`

# Scène-test 04 — Pas de prise

**NON CANON — fiction.** Test d'échec d'une influence.

Avarice attendit que le directeur lise la proposition de bonus. L'argent était assez important pour justifier l'offre, assez modeste pour préserver la trésorerie.

Il amplifia l'anticipation du gain.

Le directeur regarda la somme. Il pensa aux employés dont on avait gelé les salaires. L'enthousiasme qu'Avarice cherchait à provoquer disparut sous une fatigue plus ancienne.

— Je refuse, dit-il.

Avarice recommença, plus tard, auprès du président du comité de rémunération. Cette fois, l'émotion prit : le président sentit une irritation immédiate devant ce refus qu'il interpréta comme une leçon de morale.

La discussion se dégrada. Le bonus resta bloqué, mais le directeur perdit un allié.

— Tu n'as pas obtenu le bonus, dit Emprise.

— Non. J'ai obtenu une distance.

Le directeur n'apprendrait jamais pourquoi son refus avait coûté si cher.

**Lecture visible** : intérêts divergents et dynamique institutionnelle. **Lecture fantastique** : une prise directe rate; une prise latérale modifie le rapport de force.

---

## Fichier : `material/scene_tests/05_l_economie_du_pardon.md`

# Scène-test 05 — L'économie du pardon

**NON CANON — fiction.** Test de la destination émotionnelle sans prêche.

L'homme avait insulté son frère, puis passé vingt ans à appeler cela une décision. Il avait des raisons : la fatigue, une dette, l'orgueil, les mots choisis trop vite. Il en avait trouvé d'autres avec les années.

Le jour où son frère lui répondit enfin, il sentit d'abord la vieille colère. Puis un chagrin inattendu l'emporta. Il s'excusa.

Compassion revendiqua cet instant. Orgueil protesta qu'il avait déjà usé toute son énergie à entretenir la rancune. Aucun des deux ne pouvait démontrer que l'autre s'était trompé.

Les frères ne rattrapèrent pas vingt ans. Ils prirent un café.

— C'était donc si peu? demanda Orgueil.

— C'était ce qu'il restait, répondit Compassion.

**Lecture visible** : le pardon ne répare pas les années. **Lecture fantastique** : même l'élan vers la paix peut avoir été influencé.

---

## Fichier : `material/scene_tests/README.md`

# Scènes-tests (toutes NON CANON)

Ces essais mesurent la **densité**, le **ressenti**, l'**influence distribuée** et la **relativité des conséquences**, sans constituer du manuscrit.

1. `01_la_norme.md` : un ange protège et produit un dommage économique.
2. `02_le_refus.md` : un démon rompt une habitude et ouvre un bien non prévu.
3. `03_l_interprete.md` : un relais minuscule et une conséquence diplomatique, **entièrement fictifs**.
4. `04_pas_de_prise.md` : influence ratée puis stratégie latérale.
5. `05_l_economie_du_pardon.md` : effet d'apaisement qui n'efface pas le passé.

Réviser en coupant plutôt qu'en ajoutant du décor. La juxtaposition des deux lectures doit être lisible sans paragraphes d'explication dans le roman.

---

## Fichier : `material/scenes/README.md`

# Scenes — réserve

Espace de travail **non canonique**. Toute idée intégrée au récit doit d’abord passer par `core/07_AMBIGUITIES_AND_DECISIONS.md` et le brief concerné.

---

# Manuscrit

## Fichier : `manuscript/README.md`

# Manuscrit — réservé au texte littéraire approuvé

Structure suggérée (à adapter) :

- `part_1/`
- `part_2/`
- `part_3/`

Les briefs ne sont **pas** des chapitres. On garde hors de ce dossier les hypothèses, vérifications, fiches d'idées et dialogues non validés. La dernière signature King Klown est documentée dans `core/13_ENDING_PROTOCOL.md`, mais ne doit être introduite dans le manuscrit **qu'à la fin effective du projet**.

---
