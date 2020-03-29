from needleman_wunsch import *
import time
import sys

if __name__ == "__main__":
	DATASET = sys.argv[1]
	with open(DATASET, "r") as dataset:
		lines = (line.rstrip() for line in dataset)
		lines = (line for line in lines if line)		#On ignore les lignes blanches
		lines = list(lines)
		if len(lines)%2 != 0 :
			lines = lines[:-1]							#On ignore la dernière ligne si elles sont en nombre impair
		t = time
		count = 1
		while len(lines) != 0:
			top = lines.pop(0) 			# On récupère les lignes deux par deux
			bottom = lines.pop(0)
			start_time = time.time()
			ruler = Ruler(top, bottom)
			ruler.compute()				# On compile la règle

			print(f"====== example # {count} - distance = {ruler.distance} \n")
			rtop , rbottom = ruler.report()
			print(rtop)
			print(rbottom)
			print("Execution time: %s seconds" % (time.time()- start_time))  
			#On affiche le temps de calcul pour la paire
			
			count += 1