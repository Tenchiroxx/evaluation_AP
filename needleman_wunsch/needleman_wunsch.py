# -*- coding: utf-8 -*-
import numpy as np
from colorama import Fore, Style


def red_text(text):
	return f"{Fore.RED}{text}{Style.RESET_ALL}"


class Ruler:

	"""Cette classe est utilisée pour mesurer la distance entre deux chaînes d'ADN,
	c'est-à-dire le nombre de substitutions et de délétions nécessaires pour passer
	d'une chaîne à l'autre."""

	def __init__(self, top, bottom):
		"""Initialise la classe Ruler.

		Keyword arguments :
		top (string) -- La première chaîne d'ADN.
		bottom (string) -- La deuxième chaîne d'ADN."""

		self.top = top
		self.bottom = bottom
		self.checkcompute = False
		# Attribut permettant de vérifier que compute est bien appliqué avant report.

	def __getattr__(self, name: str):

		value = self.__dict__.get(name) # Get internal dict value matching name.
		if name == "distance":

			if not value:
				raise AttributeError(f"Make sure to compute your Ruler "\
									 "by using ruler.compute() before using ruler.distance")
				# Garde fou pour éviter d'appeler l'attribut distance sans qu'il n'existe
		else:
			if not value:
				raise AttributeError(
					f'{self.__class__.__name__}.{name} is invalid.')
				# Garde fou pour éviter les attributs qui n'existent pas.
		return value

	def compute(self):

		"""Cette classe permet de compiler la règle 'ruler'. 

		Attributs générés :

		self.distance -- La distance entre top et bottom
		self.top et self.bottom -- Les attributs sont complétés : 
		les délétions sont marquées par des tirets rouges, 
		et les substitutions sont remplacées par la bonne lettre en rouge.""" 

		s = 1  # On fixe le cout en distance d'une substitution.
		d = 1  # On fixe le cout en distance d'une délétion.

		# On définit la matrice pour déterminer l'alignement de score minimal
		F = np.zeros((len(self.top), len(self.bottom)))
		for j in range(len(self.bottom)):
			F[0][j] = d*j
		for i in range(len(self.top)):
			F[i][0] = d*i
		for i in range(1, len(self.top)):
			for j in range(1, len(self.bottom)):
				F[i][j] = min(F[i-1][j-1] + s*(1-int(self.top[i]
													 == self.bottom[j])), F[i][j-1]+d, F[i-1][j]+d)

		# On initialise les chaÎnes top et bottom corrigées
		alignment_top, alignment_bottom = f"", f""
		i = len(self.top) - 1
		j = len(self.bottom) - 1
		self.distance = F[i][j]
		while (i >= 0 and j > 0):
			# On remonte la matrice F pour calculer la distance, et les substitutions et délétions
			if (i >= 0 and j > 0 and F[i][j] == F[i-1][j-1] + s*(1-int(self.top[i] == self.bottom[j]))):
				if self.top[i] == self.bottom[j]:
					alignment_top = self.top[i] + alignment_top
					alignment_bottom = self.bottom[j] + alignment_bottom
				else:
					alignment_top = red_text(self.top[i]) + alignment_top
					alignment_bottom = red_text(self.bottom[j]) + alignment_bottom
				i = i - 1
				j = j - 1

			elif (i >= 0 and F[i][j] == F[i-1][j] + d):
				alignment_top = self.top[i] + alignment_top
				alignment_bottom = red_text(f"=") + alignment_bottom
				i = i - 1

			else:
				alignment_top = red_text(f"=") + alignment_top
				alignment_bottom = self.bottom[j] + alignment_bottom
				j = j - 1

		while i >= 0: # On gère le cas où les indices i et j ne sont plus tous les deux non-nuls.
			if j == 0:
				if self.top[i] == self.bottom[j]:
					alignment_top = self.top[i] + alignment_top
					alignment_bottom = self.bottom[j] + alignment_bottom
				else:
					alignment_top = red_text(self.top[i]) + alignment_top
					alignment_bottom = red_text(self.bottom[j]) + alignment_bottom
				j -= 1
			else:
				alignment_top = self.top[i] + alignment_top
				alignment_bottom = red_text(f"=") + alignment_bottom
				j -= 1
			i -= 1
		while j >= 0:
			alignment_top = f"=" + alignment_top
			alignment_bottom = self.bottom[j] + alignment_bottom
			j -= 1
		self.top, self.bottom, self.checkcompute = alignment_top, alignment_bottom, True

	def report(self):

		"""Permet de retourner les chaînes modifiées.

		Returns :
		self.top (string) -- La chaîne du haut modifiée
		self.bottom (string) -- La chaîne du bas modifiée"""
		
		if not self.checkcompute: #Garde fou pour s'assurer qu'on a bien compilé la règle.
			raise AttributeError("Make sure to compute your Ruler"\
								 " by using ruler.compute() before using ruler.report()")
		return self.top, self.bottom