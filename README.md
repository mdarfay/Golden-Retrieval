# golden-retrieval

Text Information Retrieval project of 3INFO TALEO

# Fichiers générés
## Lexique *lexique.txt*
Le lexique contient chaque mot utile du lexique, ainsi que le nombre de documents dans lequel le mot apparaît.
`mot, nb de documents présents`

## Indexs *index.DOC* ou *index.QRY*
Indexs inversés :
```word1,doc i,score dans le doc i, doc j, score dans le doc j,...
word2,doc k,score dans le doc k```

On peut générer les indexs "dans l'ordre", par document, avec chaque mot, mais cela prend plus de place à stocker.

## Résultat = result.res
`requete, document pertinent, score du document`


###
./eval.pl CISI_dev.REL ../Generated_files/result.res | tail -n2 | head -n1 | awk '{print $13}'

13 = F mesure (must prio)
15 = précision à 1
17 = précision à 5

POS TAGGING? (séparer verbes et autres types de mots), et sinon changer le TF/IDF
TF : au lieu de compter nb de mots, juste regarder 0/1 peut être mieux
