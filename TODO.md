# Installer des packages
`pip3 install nompackage [--user]` (pour mettre dans notre home utiliser l'option)

# Ressources utiles
https://machinelearningmastery.com/clean-text-machine-learning-python/

# A refléchir :
- virer les chiffres à virgules ou les garder ? / garder seulement les années ?
- pour l'instant lexique en minuscules, à modifier si détection noms propres

# Scripts à faire
## Script 1 : Indexation
Faire l'indexation des documents et des requêtes. Créer des vecteurs qui représentent chaque document par rapport aux mots du lexique.


- ~~Lister les mots de tous les documents (faire un lexique)~~
- ~~Virer la stopword list~~
- Enlever les mots les plus fréquents (**tuning possible ici**)
- checker les mots contenus dans tous les documents (ou la majorité)

## Script 2 : Moteur de recherche
Utilise les index créés pour faire la relation entre requêtes et documents 
