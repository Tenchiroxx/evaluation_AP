import numpy.random as rd
import sys

def creation(n, errorrate = 0.01):

	"""Cette fonction permet de créer deux créer deux chaînes d'ADN de longueur n. 
	La seconde est une copie de la première, à laquelle on a affecté
	des erreurs (substitutions ou délétions) avec un taux d'erreur donné.

	Keyword arguments :
	n (int) -- Longueur désirée des chaînes
	errorate (float) -- Taux d'erreur désiré dans la deuxième chaîne d'ADN"""
	
	top = ""
	bottom = ""
	nucleotides = ["A", "C", "T", "G"]             # On initialise la liste des différents nucléotides
	for i in range(n):

		nucleotide = rd.choice(nucleotides)			# On choisit un nucléotide au hasard
		top += nucleotide
		t = rd.random(1)

		if t < errorrate/100:
			bottom += rd.choice(nucleotides+[""])   
			#Avec une probabilité d'environ errorrate %, on effectue une délétion ou une substitution sur le brin bottom
		else : 
			bottom += nucleotide

	with open("dataset.txt", "a") as dataset:  # On écrit les deux chaînes d'ADN dans dataset
		
		dataset.write(top+"\n")
		dataset.write(bottom+"\n")


if __name__ == "__main__":
	
	creation(int(sys.argv[1]), int(sys.argv[2]))  
	# Pour lancer la creation dans un terminal, saisir la commande "python creationADN.py n errorrate"



