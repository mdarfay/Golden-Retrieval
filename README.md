# golden-retrieval

Projet de récupération d'information textuelle, réalisé durant la 3ème année du cursus Informatique à l'INSA Rennes, France, 2019.
Ce projet s'inscrit dans le cours de Traitement Automatisé du Langage Ecrit et Oral.

Authors: [Pierre-Antoine Cabaret](https://github.com/inkaru), [Matthieu Darfay](https://github.com/mdarfay), [Emilie Hummel](https://github.com/unegregre) and [Zoé Levrel](https://github.com/zlevrel).

## Description
L'objectif était de construire un petit moteur de recherche textuel, durant 3 sessions de travaux pratiques.
Un sous-ensemble de 30 requêtes était fourni afin d'ajuster les paramètres de notre système. L'ensemble complet des requêtes ayant servi à évaluer notre moteur de recherche était fourni seulement durant 24h, afin de paramétrer au mieux le moteur de recherche pour obtenir les meilleurs résultats possibles.
Pour chaque requête, le système devait être en mesure de fournir une liste classée de documents par pertinence par rapport à la requête.

_PS : Le nom du projet provient d'un mauvais jeu de mots basé sur la ressemblance entre "Retriever" et "Retrieval", respectivement issus de "Golden Retrieval" (race de chien) et de "Text Information Retrieval project" (nom du projet dans le cours)._

## Résultats obtenus
Le système était évalué sur plusieurs mesures, afin de déterminer son efficacité. Les mesures en questions sont:
- la précision,
- le rappel,
- la F-mesure,
- la précision à 1 (le premier document rendu est-il pertinent ?),
- et la précision à 5 (pourcentage de documents pertinents parmi les 5 premiers proposés).

Le système devait permettre d'optimiser deux mesures en particulier : la F-mesure et la précision à 5. Les résultats obtenus par notre moteur de recherche sur l'ensemble final des requêtes sont présentés ci-dessous.

| Gold standard | Hypothèse | Corrects | Précision | Rappel | F-mesure | P@1 | P@5 |
|---------------|-----------|----------|-----------|--------|----------|-----|-----|
| 3114          | 4573      | 718      | 15.7      | 23.1   | 18.7     | 29  | 25  |

_Gold standard : Vérité terrain, dont il faut s'approcher._
_Hypothèse : nombre de documents proposés par notre moteur._
_Corrects : nombre de documents pertinents parmi ceux proposés._

Les résultats obtenus sont très bons et correspondent à ceux attendus pour le projet.

## Fonctionnalités détaillées
### Création du lexique
**Fichier concerné :** normal_lexiquing.py
**Fichiers utilisés :** CISI_dev.QRY, CISI.ALLnettoye
**Fichiers générés :** CISI_dev.QRY_normalized, CISI.ALLnettoye_normalized, CISI.ALLnettoye_lexique
Les documents sont stematisés par l’outil [nltk](https://www.nltk.org/). Certains mots sont supprimés, tels que ceux apparaissant dans la _stopWordList_ et les nombres ne représentant pas des dates. Les occurences de chaque mot sont calculées pour ne conserver que les mots compris entre les 2 variables ajustables `freqMin` et `freqMax` (variables n’intervenant qu’au moment de l’indexing, pour ne pas générer à nouveau tout le lexique lors de leur ajustement).
Les requêtes sont également stematisées puis réduites par la _stopWordList_ et la suppression de certains nombres.


### Méthode d’indexation
**Fichier concerné :** indexing.py
**Fichiers utilisés :** CISI_dev.QRY_normalized, CISI.ALLnettoye_normalized, CISI.ALLnettoye_lexique
**Fichiers générés :** index.DOCS, index.QRYS
Le lexique est récupéré et utilisé pour l’indexation. Les documents sont parcourus un par un et un dictionnaire avec les mots croisés et leur score leur est associé. La même chose est faite avec les requêtes. Les scores sont calculés par un système de TF.IDF qu’il est possible de pondérer par 3 variables : `weigthTF`, `weightIDF` et `weightTitle`. Ce dernier paramètre permet d’accorder plus d’importance aux mots présents dans le titre des documents et des requêtes.


### Mesure de similarité
**Fichier concerné :** research_engine.py
**Fichiers utilisés :** index.DOCS, index.QRYS
**Fichier généré :** result.REL
Les index des documents et des requêtes sont récupérés. Chaque requête est croisée à chaque document. Le cosinus de leur index respectif est calculé. Les meilleures associations _(requête,document)_ sont ensuite sélectionnées grâce à un seuil qu’il est possible d’ajuster.

### Outils utilisés
**Externe :** [nltk](https://www.nltk.org/) pour la stematisation des documents et requêtes

**Internes :**
• tools.py : contient une fonction d’inversion de double dictionnaire
• controller.py : appelle indexing.py, research_engine.py puis eval.pl en passant en paramètres les variables ajustables ; permet d’ajuster les paramètres par une commande en voyant le résultat directement
• DogDogGo.py : boucle sur controller.py en modifiant les valeurs des paramètres ; renvoie les paramètres associés au meilleur résultat de f_mesure obtenu

13 = F mesure (must prio)
15 = précision à 1
17 = précision à 5

POS TAGGING? (séparer verbes et autres types de mots), et sinon changer le TF/IDF
TF : au lieu de compter nb de mots, juste regarder 0/1 peut être mieux


controller.py 0.0055 5 1 0 180 -> 21.1%

controller.py 0.006200000000000003 5 1 0 180 -> 21.5%
