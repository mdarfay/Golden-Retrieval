#!/usr/bin/python3
# -*- coding: utf-8 -*-
from tools import *
import operator
from math import sqrt



#TODO : Paramètre à ajuster 
SEUIL = 0.14




"""
---------FONCTIONS UTILISEES---------
"""

# Réécriture en dictionnaire, produit {word : {doc:score ; doc2 : score ; ...} ...}
def rewrite_dict(tab) :
	dico = dict()
	for string in tab:
		string_tab = string.split(",") #string_tab = [word ; doc ; score ; doc2 ; score2 ; ...]
		word = string_tab[0]
		dico[word] = dict() # création du dictionnaire associé à chaque mot
		# remplissage du dictionnaire associé à chaque mot
		for i in range(1,len(string_tab),2):
			dico[word][int(string_tab[i])] = float(string_tab[i+1])

	return dico



# Produit scalaire entre un document et une requête :
def scalar_product(doc, qry) : # doc et qry sont des dico de la forme {word : score ; word2 : score2 ; etc.}
	result = 0
	for word in qry :
		if word in doc :
			result += qry[word] * doc[word]

	return result


# Norme d'un vecteur (sous la forme d'un dictionnaire, par exemple {word:score ; word2;score2; ...})
def norme(dico) :
	result = 0
	for word in dico :
		result += dico[word] * dico[word]
	return sqrt(result)







"""
-----------------MAIN-----------------
"""


# Importation des fichiers index 
index_docs_file = open("../Generated_files/index.DOCS")
index_docs_tab = index_docs_file.read().splitlines()
index_docs_file.close()

index_qrys_file = open("../Generated_files/index.QRYS")
index_qrys_tab = index_qrys_file.read().splitlines()
index_qrys_file.close()

# Création des index
index_docs = reverse_double_dict( rewrite_dict(index_docs_tab) )	# {doc : {word:score ; word2;score2; ...} ; doc2 : {word5:score5; ...} ; ... }
index_qrys = reverse_double_dict( rewrite_dict(index_qrys_tab) )	# {qry : {word:score ; word2;score2; ...} ; qry2 : {word5:score5; ...} ; ... }



# Meilleurs documents par rapport aux requêtes :
associations = dict() # {qry : {doc:scalar ; doc2;scalar2 ; ...} ; ...}

for qry,dic_qry in index_qrys.items() :
	associations[qry] =  {} # initialisation dictionnaire vide
	for doc,dic_doc in index_docs.items() :
		# Score normalisé entre 0 et 1 par : produit scalaire / produit norme des vecteurs
		score_doc = scalar_product(dic_doc,dic_qry) / (norme(dic_doc) * norme(dic_qry))

		if (score_doc > SEUIL) : #SEUIL est une variable fixée tout en haut du script 
			associations[qry][doc] = score_doc


# Ecriture dans un fichier des résultats 
fichier = open("../Generated_Files/result.res","w")


for qry in sorted(associations) :
	for doc in sorted(associations[qry]) : 
		fichier.write(str(qry) + "		" + str(doc) + "		" + str(associations[qry][doc]) + "\n")

fichier.close()
					
			
			





				
		
