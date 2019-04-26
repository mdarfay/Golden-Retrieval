from collections import defaultdict


# Inverse un double dictionnaire
def reverse_double_dict(dico):
	flipped = defaultdict(dict)
	for key, val in dico.items():
		for subkey, subval in val.items():
		    flipped[subkey][key] = subval
		    
	return flipped
