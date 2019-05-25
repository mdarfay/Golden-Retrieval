import os
import numpy as np
import re

# Execute "normal_lexiquing une seule fois
#os.system("python3 normal_lexiquing.py")

regex = re.compile(r"(.+)%")

bestSeuil = 0
bestTF = 1
bestIDF = 1
bestFreqMax = 1020
bestF = 0

# Boucle de variation du poidsTF entre 1 et 5 (pas de 0.1)
for poidsTF in np.arange(5,6,0.5):
    # Boucle de variation de la freq max
    for freqMax in np.arange(100,300,10):
        # Boucle de variation du seuil entre 0 et 1 (pas de 0.0005)
        for seuil in np.arange(0.005,0.008,0.0002):
            readFmesure = os.popen("python3 controller.py "+str(seuil)+" "+str(poidsTF)+" 1 0 "+ str(freqMax) +" | tail -n2 | head -n1 | awk \'{print $13}\'", "r").read()
            if(re.match(regex,readFmesure) != None):
                Fmesure = float(re.match(regex, readFmesure).group(1))
                #print(Fmesure)
                if(bestF < Fmesure):
                    bestF= Fmesure
                    bestSeuil = seuil
                    bestTF = poidsTF
                    bestFreqMax = freqMax

print("Best Fmesure : "+str(bestF)+" with seuil="+str(bestSeuil)+" poidsTF="+str(bestTF)+" freqMax="+str(bestFreqMax))