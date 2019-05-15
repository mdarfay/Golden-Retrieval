#!/usr/bin/python3
# -*- coding: utf-8 -*-
from tools import *
import operator

# Importation des fichiers index 
index_docs_file = open("./index.DOCS")
index_docs_tab = index_docs_file.read().splitlines()
index_docs_file.close()

index_qrys_file = open("./index.QRYS")
index_qrys_tab = index_qrys_file.read().splitlines()
index_qrys_file.close()


# Réécriture en dictionnaire
def rewrite_dict(tab) :
	dico = dict()
	for string in tab:
		string_tab = string.split(",") #string_tab = [word ; doc ; code_doc ; doc2 ; code_doc2 ; ...]
		word = string_tab[0]
		dico[word] = dict() # création du dictionnaire associé à chaque mot
		# remplissage du dictionnaire associé à chaque mot
		for i in range(1,len(string_tab),2):
			dico[word][string_tab[i]] = float(string_tab[i+1])

	return dico



# Produit scalaire entre un document et une requête :
def scalar_product(doc : dict, qry : dict) : # doc et qry sont des dico de la forme {word : score ; word2 : score2 ; etc.}
	result = 0
	for word in doc :
		if word in qry :
			result += 1  # FIXME : ceci n'est pas du tout un produit scalaire 

	return result



# Création des index
index_docs = reverse_double_dict( rewrite_dict(index_docs_tab) )	# {doc : {word:score ; word2;score2; ...} ; doc2 : {word5:score5; ...} ; ... }
index_qrys = reverse_double_dict( rewrite_dict(index_qrys_tab) )	# {qry : {word:score ; word2;score2; ...} ; qry2 : {word5:score5; ...} ; ... }



# Meilleurs documents par rapport aux requêtes :
associations = dict() # {qry : {doc:scalar ; doc2;scalar2 ; ...} ; ...}

for qry in index_qrys :
	associations[qry] = {"1" : 0 , "2" : 0, "3" : 0} # 3 documents par requête
	for doc in index_docs :
		scalar_doc = scalar_product(doc,qry)

		# Remplace le minimum par le produit scalaire calculé s'il est le plus grand
		indice_min = min(associations[qry].items(), key=operator.itemgetter(1))[0] # Renvoie la clef de la plus petite valeur
		if(scalar_doc > associations[qry][indice_min]) :
			del associations[qry][indice_min]
			associations[qry][doc] = scalar_doc




# Ecriture dans un fichier des résultats 
fichier = open("result","w")

for qry in associations :
	for doc in associations[qry] : 
		fichier.write(qry + "		" + doc + "		" + str(associations[qry][doc]) + "\n")

fichier.close()
					
			
			





				
		
