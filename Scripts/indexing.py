#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
import time
from tools import *

# Importation du lexique
lexique_file = open("../Generated_files/lexique.txt")
lexique = lexique_file.read().splitlines() #recupere les mots sans les \n
lexique_file.close()


# Ouverture des documents à parcourir
docs = "../Data_files/CISI.ALLnettoye"
queries = "../Data_files/CISI_dev.QRY"

# Extrait les mots du lexique de chaque ligne et stocke dans le dictionnaire du doc courant
def extract_w_line(mots, line):
	for mot in line.split():
		if mot in lexique:
			mots[mot] = "1"	#TODO 1 = score du mot, ici juste un boolean
			
			
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
    
	index = {}   # liste de tous les documents, entête exclu
	mots = {}    # liste des lignes d'un document
	num_doc = -1

	# sépare les différents documents dans la liste docs et rempli leur dict de mots associé
	for line in data:  
		match = re.search(regex, line)
		if match:
			num_doc = match.group(1)
			mots = {}
			index[num_doc] = mots
		else:
			extract_w_line(mots, line)

	data.close()

	# Inverse l'index pour le stockage à l'envers
	reverse_index = reverse_double_dict(index)
	
  # Ecriture de l'index final
	res = open("../Generated_files/index."+extension, "w")
	write_dict(res, reverse_index)
	res.close()



# APPEL DU PROGRAMME SUR LES FICHIERS

#main_indexing("./texttest", "TEST")
startDocs = time.time()
main_indexing(docs, "DOCS")
endDocs = time.time()
print("Index DOCS done, in : ", endDocs-startDocs, " seconds")
main_indexing(queries, "QRYS")
endQuery = time.time()
print("Index QUERIES done, in : ", endQuery-endDocs, " seconds")
print("Total exec time = ", endQuery-startDocs, " seconds")





