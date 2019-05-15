#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
import time
from tools import *

# Importation du lexique
def readLexique():
	lexique_file = open("../Generated_files/lexique.txt")
	lex = lexique_file.read().splitlines() #recupere les mots_doc sans les \n
	lexique = {}
	for line in lex:
		line = line.split(",")
		lexique[line[0]] = line[1]
	lexique_file.close()
	return lexique


# Extrait les mots_doc du lexique de chaque ligne et stocke dans le dictionnaire du doc courant
def extract_w_doc(mots_doc, doc):
	for ligne in doc:
		for mot in ligne.split():
			if mot in lexique:
				mots_doc[mot] = "1"	#TODO 1 = score du mot, ici juste un boolean
				
			
# Ecrit proprement le double dict dans le fichier de sortie
# FORMAT : 1 mot par ligne => mot,doci,score_in_doci,docj,score_in_docj
def write_dict(fichier, dico):
    for elem in dico:
        fichier.write(elem)
        for obj in dico[elem]:
            fichier.write(","+obj+","+dico[elem][obj])
        fichier.write("\n")
	

def main_indexing(path, extension):
	# regex pour les délimitations de documents
	regex = re.compile(r"\.I\s(\d+)\s$")
	  
	# Separation de tous les documents
	data = open(path)
    
	index = {}	# index { doc : mots }
	docs = {}	# dico de tous les docs : { num : [texte_doc] }
	texte_doc = "" 
	mots_doc = {}	# liste des lignes d'un document
	num_doc = -1

	# sépare les différents documents dans la liste docs et rempli leur dict de mots_doc associé
	for line in data:
		match = re.search(regex, line)
		if match:
			num_doc = match.group(1)	# récupère le numéro du doc
			mots_doc = {}
			index[num_doc] = mots_doc
			texte_doc = []
			docs[num_doc] = texte_doc
		else:
			texte_doc.append(line.rstrip('\n'))
	
	for num in docs:	# clé de docs = num des doc
		extract_w_doc(index[num], docs[num])	# on envoie le dico de mots associé au doc ET le document en entier
	
	data.close()

	# Inverse l'index pour le stockage à l'envers
	reverse_index = reverse_double_dict(index)
	
	# Ecriture de l'index final
	res = open("../Generated_files/index."+extension, "w")
	write_dict(res, reverse_index)
	res.close()



# APPEL DU PROGRAMME SUR LES FICHIERS
lexique = readLexique()

# Ouverture des documents à parcourir
docs = "../Data_files/CISI.ALLnettoye"
queries = "../Data_files/CISI_dev.QRY"

"""
main_indexing("../Generated_files/texttest", "TEST")
"""
main_indexing(docs, "DOCS")
main_indexing(queries, "QRYS")




