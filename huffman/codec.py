from parcours import parcours
import struct


class TreeBuilder:
	""""Cette classe permet de créer l'arbre binaire associé au codage de Huffman"""

	def __init__(self, text):

		self.text = text


	def tree(self):

		"""Cette fonction permet de générer l'arbre binaire associé au texte d'entrée

		Attribut modifié :
		self.tree (dict) -- Cet attribut est finalement un dictionnaire ayant pour clés 
		les différentes lettres du texte d'entrée, et pour valeurs, les codages de Huffman associés."""

		occ = dict()
		for i in self.text:      # On crée un dictionnaire qui dénombre le nombre 
			if i in occ:		 # d'occurences de chaque caractère du texte.
				occ[i] += 1
			else:
				occ[i] = 1

		#On crée autant de tas qu'il y a de lettres distinctes dans le texte.
		#Chaque tas contient une lettre et sa fréquence d'apparition

		heap = [(freq, {'value' : letter}) for (letter, freq) in occ.items()] 
		heap.sort(key=lambda tup: tup[0])

		while len(heap) > 1: #On regroupe les deux tas de plus faible poids
							 #On itère jusqu'à n'avoir plus qu'un seul tas
			freq1, left = heap.pop(0) 
			freq2, right = heap.pop(0)
			heap = heap + [(freq1 + freq2, {"0" : left, "1" : right})]
			heap.sort(key=lambda tup: tup[0])

		_, self.tree = heap[0]
		
		return parcours(self.tree)

class Codec:

	"""Cette classe permet de créer un encodeur/décodeur avec un codage donné."""

	def __init__(self, binary_tree : dict):  
	#L'arbre binaire est un dictionnaire qui contient les feuilles en clés, et leur code associé en valeur
		self.binary_tree = binary_tree
		self.swap_binary_tree = dict([(value, key) for key, value in binary_tree.items()]) 
	
	def encode(self, text):
		"""Cette fonction permet d'encoder un texte à partir du codage donné.

		Keyword argument:
		text (str) -- Le texte à encoder

		Returns :

		encoded (str) -- La phrase mise sous forme d'une chaîne de caractères constituée de 0 et de 1."""
		encoded = str()
		for letter in text:
			encoded += self.binary_tree[letter]

		return encoded

	def decode(self, encoded):
		"""Cette fonction permet décoder un texte à partir du codage donné.

		Keyword argument:

		encoded (str) -- Le texte à décoder

		Returns:

		decoded (text) -- Le texte décodé.
		"""

		decoded = str()
		temp = "" 
		for i in range(len(encoded)):
			bit = encoded[i]
			temp = temp+bit
			if temp in self.swap_binary_tree.keys():
				decoded += self.swap_binary_tree[temp]
				temp = ""

		return decoded


	def encode_bin(self, text : str):

		encoded = str()

		for letter in text:
			encoded += self.binary_tree[letter]
		
		encoded = struct.pack("!H",  int("1"+encoded, 2)) 
		#On rajoute un 1 au début de encoded pour éviter que les 0 au début de encoded ne deviennent muets.

		return encoded

	def decode_bin(self, encoded : bytes):

		decoded = str()
		temp = "" 
		encoded = bin(struct.unpack("!H", encoded)[0])[3:]
		#On transforme le texte encodé dans des octets en chaîne de caractères.

		for i in range(len(encoded)):

			bit = encoded[i]
			temp = temp+bit

			if temp in self.swap_binary_tree.keys():

				decoded += self.swap_binary_tree[temp]
				temp = ""

		return decoded
