#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import division
import sys
import re
import nltk

# Stopword list
nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
stopwordslist = stopwords.words("english")
stopwordslist.append("NaN")

# regex pour les délimitations de documents
regex = re.compile(r"\.I\s\d+\s$");

#Parametre
filename = '../Data_files/CISI.ALLnettoye'
#filename = '../Generated_files/texttest'



def add(dictionnaire, ajout,docs):
    cpt=0
    if ajout not in dictionnaire:
        for doc in docs:
            found = False
            if ajout in doc.split():
                found = True
            if found:
                cpt += 1 
        dictionnaire[ajout] = cpt

# table de traduction pour enlever les car. spéciaux, remplace les '-' par des espaces
table = str.maketrans('-',' ',"!\"#$%&'()*+,./:;<=>?@[\]^_`{|}~")  # table de traduction pour enlever les car. spéciaux

def removeSpecialChar(line):
    new_line = ''
    for word in line:
        new_line += (word.translate(table))
    return new_line

def removeFrequentWords(dictio, list, percent):
    todel = []
    for word in dictio:
        present = 0
        for doc in list:
            if word in doc.split():
                present += 1
        if present >= percent*len(list):
            print(word + ' ' + str(present))
            todel.append(word)
    for wordtodel in todel:
        del dictio[wordtodel]  #supprime l'entrée si le mot est dans tous les documents
    return dictio

def removeCommonWords(text):
    string=''
    if text not in stopwordslist:
        string +=text+' '
    return string

def normalizeText(filename):
    print(filename)
    
    output = open('../Generated_files/'+filename+'_normalized','w')
    input=open(filename, 'r')

    text = input.readlines()
    porter = PorterStemmer()

    for line in text:
        if not(re.search(regex,line)):
            newline = removeSpecialChar(line)
            newline = newline.lower()
            newline = removeCommonWords(newline)
            for word in newline.split():
                stemmed = porter.stem(word)
                output.write(stemmed + " ")
            output.write('\n')
        else:
            output.write(line)


dico = dict()
separator = ' '

lexi = open('../Generated_files/lexique', 'w')
normalizeText(filename)
data = open(filename+'_normalized').readlines()
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
    for word in doc.split():
        add(dico, word, docs)     # ajout dans le lexique du mot en minuscules (à modifier plus tard)


for w in sorted(dico):      # écriture dans le fichier, dans l'ordre alphabétique
    lexi.write(w + "," + str(dico[w]) + "\n") #version avec la fréquence
    #lexi.write(w+"\n")	#version avec juste les mots