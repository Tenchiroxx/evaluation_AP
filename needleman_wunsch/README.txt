Comment rendre le coût des substitutions et des délétions paramétrable ?
	Dans la classe Ruler, la fonction __init__ pourrait prendre en argument s et d,
	respectivement le coût d'une substitution et d'une délétion.
	On introduirait alors les attributs de classe ruler.s et ruler.d tels que ruler.s = s
	et ruler.d = d.
	Ces attributs de classe pourraient ainsi être utilisés pour calculer la matrice 
	d'alignement de score maximal.
	Pour utiliser bundle.py il faudrait alors saisir la commande "python bundle.py s d"
	qui se serivait de la commande Ruler(top, bottom, s, d)