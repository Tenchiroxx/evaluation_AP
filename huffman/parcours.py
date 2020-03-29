def parcours(arbre, code = ""):

		"""Cette fonction récursive permet de parcourir un arbre binaire et d'en relever chaque feuille. 
		Il crée ainsi un dictionnaire avec la feuille de l'arbre en clé, 
		et le code associé pour parvenir à la feuille.

		Keyword arguments : 
		arbre (dict) -- L'arbre binaire à parcourir
		code (str) -- Le code utilisé pour parvenir jusqu'au noeud actuel de l'arbre

		Returns :
		liste_feuilles (dict) -- Un dictionnaire contenant les feuilles, et le code associé."""

		liste_feuilles = dict()

		if "value" in arbre.keys():  		#Si on se trouve sur une feuille de l'arbre, 
			feuille = arbre["value"]		#on ajoute cette feuille au dictionnaire des feuilles, 
			liste_feuilles[feuille] = code  #et on renseigne son code

		else :								#Si on se trouve sur un noeud, on parcours chacune des branches sur le noeud.
			for key in arbre.keys():	
				liste_temp = parcours(arbre[key], code+key)  # On applique parcours au sous-dictionnaire, 
				for key1 in liste_temp.keys():				 # en prenant en compte qu'on est allé à droite ou à gauche.
					liste_feuilles[key1] = liste_temp[key1]  # On ajoute les feuilles trouvées en descendant l'arbre
		
		return liste_feuilles