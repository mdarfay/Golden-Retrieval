import os
import numpy as np
import re

# Execute "normal_lexiquing une seule fois
#os.system("python3 normal_lexiquing.py")

regex = re.compile(r"(.+)%")

bestSeuil = 0
bestTF = 1
bestIDF = 1
bestFreqMax = 180
bestF = 0
bestTitre = 1	# FIXME
count = 0


# Boucle de variation du poidsTF entre 1 et 5 (pas de 0.1)
for poidsTF in np.arange(3, 5, 1):  # 1 5 1
    # Boucle de variation de la freq max
    for poidsTitre in np.arange(1, 25, 5):  # 1 100 2
        # Boucle de variation de IDF
        for poidsIDF in np.arange(0,1,0.1):
            # Boucle de variation du seuil entre 0 et 1 (pas de 0.0005)
            for seuil in np.arange(0.004, 0.006, 0.0005):  # 0.004 0.008 0.0005
            
                count += 1
                readFmesure = os.popen("python3 controller.py "+str(seuil)+" "+str(poidsTF)+" 1 0 180 " + str(poidsTitre) +" | tail -n2 | head -n1 | awk \'{print $13}\'", "r").read()

                if(re.match(regex,readFmesure) != None):
                    Fmesure = float(re.match(regex, readFmesure).group(1))
                    #print(Fmesure)
                    if(bestF < Fmesure):
                        bestF= Fmesure
                        bestSeuil = seuil
                        bestTF = poidsTF
                        bestTitre = poidsTitre
			

print(count)
print("Best Fmesure : "+str(bestF)+" with seuil="+str(bestSeuil)+" poidsTF="+str(bestTF)+"  bestTitre= "+str(bestTitre))

