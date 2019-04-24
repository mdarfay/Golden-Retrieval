#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import division
import sys
import re
import nltk
import string

# Stopword list
nltk.download("stopwords")
from nltk.corpus import stopwords
stopwordslist = stopwords.words("english")
stopwordslist.append("NaN")

# regex pour les délimitations de documents
regex = re.compile(r"\.I\s\d+\s$");

def add(dictionnaire, ajout):
    if ajout in dictionnaire:
        dictionnaire[ajout] += 1
    else:
        dictionnaire[ajout] = 1

# table de traduction pour enlever les car. spéciaux, remplace les '-' par des espaces
table = str.maketrans('-',' ',"!\"#$%&'()*+,./:;<=>?@[\]^_`{|}~")  # table de traduction pour enlever les car. spéciaux

def removeSpecialChar(line):
    new_line = ''
    for word in line:
        new_line += (word.translate(table))
    return new_line


dico = dict()

lexi = open('lexique.txt', 'w')
data = open('./Data_files/CISI.ALLnettoye').readlines()
docs = []   # liste de tous les documents, entête exclu
doc = []    # liste des lignes d'un document

for line in data:  # sépare les différents documents dans la liste docs
    if re.search(regex, line):
        docs.append(doc)
        doc = []
    else:
        doc.append(line)
docs.append(doc)    # ajoute le dernier document
docs.pop(0)         # supprime le 1er document vide


for doc in docs:
    for line in doc:
        line = removeSpecialChar(line)      # suppression des car. spéciaux dans les lignes
        for word in line.split():
            if word not in stopwordslist:   # si le mot n'est pas commun :
                add(dico, word.lower())     # ajout dans le lexique du mot en minuscules (à modifier plus tard)

for w in sorted(dico):      # écriture dans le fichier, dans l'ordre alphabétique
    lexi.write(w + "," + str(dico[w]) + "\n")

