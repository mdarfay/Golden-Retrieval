import os
import numpy as np
import re

# Execute "normal_lexiquing une seule fois
#os.system("python3 normal_lexiquing.py")

regex = re.compile(r"(.*)%")

bestSeuil = 0
bestTF = 1
bestIDF = 1
bestF = 0

# Boucle de variation du poidsTF entre 1 et 5 (pas de 0.1)
for poidsTF in np.arange(1,5,1):
    # Boucle de variation de poids IDF entre 1 et 5 (pas de 0.1)
    for poidsIDF in np.arange(1,5,1):
        # Boucle de variation du seuil entre 0 et 1 (pas de 0.0005)
        for seuil in np.arange(0,1,0.1):
            os.system("python3 controller.py "+str(seuil)+" "+str(poidsTF)+" "+str(poidsIDF))
            readFmesure = os.popen("../Data_files/eval.pl ../Data_files/CISI_dev.REL.. / Generated_files / result.res | tail -n2 | head -n1 | awk \'{print $13}\'", "r").read()
            print(readFmesure)
            if(re.match(regex,readFmesure) != None):
                Fmesure = int(re.match(regex,readFmesure).group())
                print(Fmesure)
                if(bestF < Fmesure):
                    bestF= Fmesure
                    bestSeuil = seuil
                    bestTF = poidsTF
                    bestIDF = poidsIDF

print("Best Fmesure : "+bestF+" with seuil="+bestSeuil+" poidsTF="+bestTF+" poidsIDF="+bestIDF)