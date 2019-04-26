import re
from collections import defaultdict

# Importation du lexique
lexique = open("./lexique.txt").read().splitlines() #recupere les mots sans les \n


# Ouverture des documents à parcourir
docs = "./Data_files/CISI.ALLnettoye"
queries = "./Data_files/CISI_dev.QRY"

# Extrait les mots du lexique de chaque ligne et stocke dans le dictionnaire du doc courant
def extract_w_line(mots, line):
	for mot in line.split():
		if mot in lexique:
			mots[mot] = "1"	#TODO 1 = score du mot, ici juste un boolean
		
			
# Inverse un double dictionnaire
def reverse_double_dict(dico):
	flipped = defaultdict(dict)
	for key, val in dico.items():
		for subkey, subval in val.items():
		    flipped[subkey][key] = subval
		    
	return flipped
			
			
# Ecrit proprement le double dict dans le fichier de sortie
# FORMAT : 1 mot par ligne => mot,doci,score_in_doci,docj,score_in_docj
def write_dict(fichier, dico):
	for elem in dico:
		fichier.write(elem)
		for obj in dico[elem]:
			fichier.write(","+obj+","+dico[elem][obj])
		fichier.write("\n")
	

def main_indexing(path, extension):
    # regex pour les délimitations de documents
	regex = re.compile(r"\.I\s(\d+)\s$")
	  
	# Separation de tous les documents
	data = open(path)
    
	index = {}   # liste de tous les documents, entête exclu
	mots = {}    # liste des lignes d'un document
	num_doc = -1

	# sépare les différents documents dans la liste docs et rempli leur dict de mots associé
	for line in data:  
		match = re.search(regex, line)
		if match:
			num_doc = match.group(1)
			mots = {}
			index[num_doc] = mots
		else:
			extract_w_line(mots, line)

	# Inverse l'index pour le stockage à l'envers
	reverse_index = reverse_double_dict(index)
	
    # Ecriture de l'index final
	res = open("index."+extension, "w")
	write_dict(res, reverse_index)
	res.close()



# APPEL DU PROGRAMME SUR LES FICHIERS

#main_indexing("./texttest", "TEST")
main_indexing(docs, "DOCS")
main_indexing(queries, "QRYS")





