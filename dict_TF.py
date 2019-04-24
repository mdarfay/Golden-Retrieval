#!/usr/bin/python3
# -*- coding: utf-8 -*-
from __future__ import division
import sys
import re
import nltk
import string

nltk.download("stopwords")
from nltk.corpus import stopwords
stopwordslist = stopwords.words("english")
stopwordslist.append("NaN")

regex = re.compile(r"\.I\s\d+\s$");

def add(dictionnaire,ajout):
	if ajout in dictionnaire:
		dictionnaire[ajout]+=1
	else:
		dictionnaire[ajout]=1
	
table = str.maketrans('', '', string.punctuation)   #table de traduction pour enlever les car. spéciaux


dico = dict()

lexi = open('lexique.txt','w')
data = open('texttest').readlines()
docs=[]
doc = []
for line in data:               #sépare les différents documents dans la liste docs
    if(re.search(regex,line)):
        docs.append(doc)
    else:
	    doc.append(line)

for doc in docs:
    for line in doc:
        for word in line.split():
            word = word.translate(table)
            if word not in stopwordslist and word is not '':
                add(dico,word)
            #print(word)

for w in sorted(dico):
    lexi.write(w+","+str(dico[w])+"\n")
