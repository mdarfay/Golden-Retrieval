#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
import time
from tools import *
import sys

# TODO : fixer les poids de TF et IDF /!\ il s'agit de puissances /!\
weightTF = 1
weightIDF = 1
weightTitle = 1 # FIXME poids du titre
freqInf = 0
freqSup = 1400

if len(sys.argv) == 3:
	weightTF = float(sys.argv[1])
	weightIDF = float(sys.argv[2])
	
if len(sys.argv) == 6:
	weightTF = float(sys.argv[1])
	weightIDF = float(sys.argv[2])
	freqInf = float(sys.argv[3])
	freqSup = float(sys.argv[4])
	weightTitle = float(sys.argv[5])

# Importation du lexique
def readLexique(pathLexique):
	lexique_file = open(pathLexique)
	lex = lexique_file.read().splitlines() #recupere les mots_doc sans les \n
	lexique = {}
	for line in lex:
		line = line.split(",")
		if freqInf < float(line[1]) < freqSup:
			lexique[line[0]] = float(line[1])
	lexique_file.close()
	return lexique
	

# Extrait les mots_doc du lexique de chaque ligne et stocke dans le dictionnaire du doc courant
def extract_w_doc(mots_doc, doc, nbDocs, titre):	# ref dico de mots, liste de lignes, int, String
	words_doc_occ = {}	# ensemble des mots du doc et leur occurence associée
	total_words = 0
	# Mettre tous les mots du doc et leur occurence
	for ligne in doc:
		for mot in ligne.split():
			total_words += 1	# on compte le nombre de mots total
			if mot in lexique:
				if mot not in words_doc_occ:
					words_doc_occ[mot] = 1
				else:
					words_doc_occ[mot] += 1
	
	
	# FIXME ajout des mots du titre au dico
	for mot in titre.split():
			total_words += 1	# on compte aussi les mots du titre
			if mot in lexique:
				if mot not in words_doc_occ:
					words_doc_occ[mot] = 1
				else:
					words_doc_occ[mot] += 1
	
	
	# Parcours tous les mots differents et les ajoute au dict de mots du doc avec calcul de TFIDF => Voir wikipedia
	# TODO : Calcul du score des mots du CORPS du doc
	for mot in words_doc_occ:
		freqMot = words_doc_occ[mot] / total_words	# nombre d'occurences du mot / nombre de mots total
		TF = freqMot
		
		IDF = nbDocs / lexique[mot]
		
		mots_doc[mot] = str( (TF ** weightTF) * (IDF ** weightIDF) )			

	
	# FIXME : Calcul du score des mots du titre
	for mot in titre.split():
		if mot in words_doc_occ:
			mots_doc[mot] = str( float(mots_doc[mot]) * weightTitle )
				
			
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
	
	dic_titles = {} # FIXME dictionnaire des titres des docs = première ligne : { n° doc : "Titre", ... }
	is_title = -1	# FIXME boolean utilisé pour le repérage du titre lors du parcours du doc

	# sépare les différents documents dans la liste docs et rempli leur dict de mots_doc associé
	for line in data:
		match = re.search(regex, line)
		if match:
			num_doc = match.group(1)	# récupère le numéro du doc
			mots_doc = {}
			index[num_doc] = mots_doc
			texte_doc = []
			docs[num_doc] = texte_doc
			
			is_title = num_doc # FIXME la prochaine ligne lue sera le titre du document (on vient d'en lire son numéro)
			dic_titles[num_doc] = "" 	# FIXME on initialise l'entrée dans le dico, en mettant une chaîne vide, remplacée à l'itération suivante par le vrai titre
		
		elif is_title != -1 :
			#print(line)
			dic_titles[is_title] = line.rstrip('\n')	# FIXME on ajoute le titre correspondant dans le dico de titres
			is_title = -1 	# FIXME on reset, on a trouvé le titre de ce doc là
			
		else:
			texte_doc.append(line.rstrip('\n'))
	
	for num in docs:	# clé de docs = num des doc
		extract_w_doc(index[num], docs[num], len(docs), dic_titles[num])	# on envoie le dico de mots associé au doc ET le document en entier # FIXME envoi du titre à part
		# PARAM = 	 référence mots du doc, document, nb de doc, titre du doc 
	
	data.close()

	# Inverse l'index pour le stockage à l'envers
	reverse_index = reverse_double_dict(index)
	
	# Ecriture de l'index final
	res = open("../Generated_files/index."+extension, "w")
	write_dict(res, reverse_index)
	res.close()



# APPEL DU PROGRAMME SUR LES FICHIERS
lexique = readLexique("../Generated_files/CISI.ALLnettoye_lexique")

# Ouverture des documents à parcourir
docs = "../Generated_files/CISI.ALLnettoye_normalized"
queries = "../Generated_files/CISI.QRY_normalized"

"""
main_indexing("../Generated_files/texttest_normalized", "TEST")
"""
main_indexing(docs, "DOCS")
main_indexing(queries, "QRYS")



