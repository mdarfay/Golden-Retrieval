""" lecture
split : sépare avec des espaces par défaut
Le premier = le mot associé au dic
puis deux par deux : doc et score
"""

"""
# Pour le calcul de distance entre les deux vecteurs dans le moteur de recherche, dict1 = requete et dict2 = doc
total = 0
for w in dict1:
	if w in dict2:
		total += dict1[w]*dict2[w] 
#penser à diviser par le produit de la norme des vecteurs
"""

import numpy as np

cpt = 0

# Boucle de variation du poidsTF entre 1 et 5 (pas de 0.1)
for poidsTF in np.arange(3,5,1):
    # Boucle de variation de la freq max
    for freqMax in np.arange(100,300,10):
        # Boucle de variation du seuil entre 0 et 1 (pas de 0.0005)
        for seuil in np.arange(0.001,0.008,0.0005):
            cpt=cpt+1

print(cpt)