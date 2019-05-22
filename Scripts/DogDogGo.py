import os
import numpy as np
import re

# Execute "normal_lexiquing une seule fois
#os.system("python3 normal_lexiquing.py")

regex = re.compile(r"(.+)%")

bestSeuil = 0
bestTF = 1
bestIDF = 1
bestF = 0

# Boucle de variation du poidsTF entre 1 et 5 (pas de 0.1)
for poidsTF in np.arange(1,3,0.1):
    # Boucle de variation de poids IDF entre 1 et 5 (pas de 0.1)
    for poidsIDF in np.arange(1,3,0.1):
        # Boucle de variation du seuil entre 0 et 1 (pas de 0.0005)
        for seuil in np.arange(0,1,(0.1)**(poidsIDF+poidsTF)):
            readFmesure = os.popen("python3 controller.py "+str(seuil)+" "+str(poidsTF)+" "+str(poidsIDF)+" | tail -n2 | head -n1 | awk \'{print $13}\'", "r").read()
            if(re.match(regex,readFmesure) != None):
                Fmesure = float(re.match(regex, readFmesure).group(1))
                #print(Fmesure)
                if(bestF < Fmesure):
                    bestF= Fmesure
                    bestSeuil = seuil
                    bestTF = poidsTF
                    bestIDF = poidsIDF

print("Best Fmesure : "+str(bestF)+" with seuil="+str(bestSeuil)+" poidsTF="+str(bestTF)+" poidsIDF="+str(bestIDF))