#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import division
import sys
import re
import nltk

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

def removeCommonWords(dictio, list, percent):
    todel = []
    for word in dictio:
        present = 1.
        for doc in list:
            if word not in doc:
                present -= 1/len(list)
        if present>=percent:
            print(word)
            todel.append(word)
    for wordtodel in todel:
        del dictio[wordtodel]  #supprime l'entrée si le mot est dans tous les documents
    return dictio


dico = dict()
separator = ' '

lexi = open('lexique.txt', 'w')
data = open('./Data_files/CISI.ALLnettoye').readlines()
#data = open('./texttest').readlines()       #for test
docs = []   # liste de tous les documents, entête exclu
doc = []    # liste des lignes d'un document

for line in data:  # sépare les différents documents dans la liste docs
    if re.search(regex, line):
        string = separator.join(doc)
        docs.append(string)
        doc = []
    else:
        doc.append(line)
docs.append(separator.join(doc))    # ajoute le dernier document
docs.pop(0)         # supprime le 1er document vide


for doc in docs:
    doc = removeSpecialChar(doc)      # suppression des car. spéciaux dans les lignes
    for word in doc.split():
        if word not in stopwordslist:   # si le mot n'est pas commun :
            add(dico, word.lower())     # ajout dans le lexique du mot en minuscules (à modifier plus tard)


# Retire les mots qui sont dans 80% des textes
dico = removeCommonWords(dico,docs,0.8)     # le dernier paramètre ajuste la sensibilité du remove

for w in sorted(dico):      # écriture dans le fichier, dans l'ordre alphabétique
    lexi.write(w + "," + str(dico[w]) + "\n")

