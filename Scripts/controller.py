import sys
import os

if( len(sys.argv) < 6):
	print("Usage : python3 DogDogGo.py <seuil> <poidsTF> <poidsIDF> <freqInf> <freqSup>\n"+
	"seuil = [0,1], poids = puissances, [1-5]")
	sys.exit()
else:
	seuil = sys.argv[1]
	poidsTF = sys.argv[2]
	poidsIDF = sys.argv[3]
	freqInf = sys.argv[4]
	freqSup = sys.argv[5]


	
os.system("python indexing.py "+poidsTF+" "+poidsIDF+" "+freqInf+" "+freqSup)
os.system("python research_engine.py "+seuil)
os.system("perl eval.pl ../Data_files/CISI_dev.REL ../Generated_files/result.res")
