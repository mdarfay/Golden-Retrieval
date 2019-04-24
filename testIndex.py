reverse_index = {
    "oui" : { "1":1 , "2":1 } ,
    "zon" : { "1":1 , "4":1 }
}

extension = "TEST"
# Ecriture de l'index final
res = open("index."+extension, "w")
res.write(str(reverse_index))
res.close()

# ecriture
for elem in reverse_index:
	print(elem,":",reverse_index[elem])


""" lecture
split : sépare avec des espaces par défaut
Le premier = le mot associé au dic
puis deux par deux : doc et score
"""


# Pour le calcul de distance entre les deux vecteurs dans le moteur de recherche, dict1 = requete et dict2 = doc
total = 0
for w in dict1:
	if w in dict2:
		total += dict1[w]*dict2[w] 
#penser à diviser par le produit de la norme des vecteurs
