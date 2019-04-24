"""
Parcourir tous les docs / req, on construit un dictionnaire pour chaque doc : {"mot" : nbOccurences dans le doc}
Dictionnaire de dictionnaire : {"n° du doc (après le .I)" : dictionnaire associé }

Ajout de la pondération aux mots => calcul du score pour chaque mot pour chaque doc //TODO tuning
@Return = dict de dict MAIS en inversé, MOT => {"doc":poids} (pour la mise en mémoire)
"""
import re

# Importation du lexique
fichier = open("./lexique.lex").readlines() # Fichier = liste de mots (un mot par ligne)
fichier.close()

lexique = []
for line in fichier:
    lexique.append(line.rstrip())


# Ouverture des documents à parcourir
docs = "./Data_files/CISI.ALLnettoye"
queries = "./Data_files/CISI_dev.QRY"


def indexing(path, extension):
    # @Param dans le open pour choisir si on fait l'index sur les docs ou les requetes
    fileToParse = open(docs).readlines()

    index = {} 

    while :
    # parcours doc
        # RECUPERER NUMERO DU DOC
        dictDoc = {}
        # remplir le dict
        # séparer les lignes en mots
        # pour chaque mot : ajout dans le dico avec val 1 si pas dedans
        index[i] = dictDoc


    fileToParse.close()

    # Inversion de l'index
    reverse_index = {}
    for mot in lexique :
        reverse_index[mot] = {}
        for doc in index :
            if mot in doc :
                reverse_index[mot][doc]=index[doc][mot]




    # Ecriture de l'index final
    res = open("index."+extension, "w")
    
    
    res.write(reverse_index)
    res.close()


indexing(docs, "DOC")
indexing(queries, "QRY")





