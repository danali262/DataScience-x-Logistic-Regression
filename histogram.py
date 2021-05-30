import pandas as pd
import numpy as np
import sys
import matplotlib.pyplot as plt
import cv2 as cv

# input checking
if len(sys.argv) != 2 :
	print ("Please provide an input file\n", end='')
	sys.exit(-1)

# reading input file from command line
input_file = pd.read_csv(sys.argv[1])
number_of_rows = len(input_file)
number_of_columns = len(input_file.columns)
subjects = ["Arithmancy", "Astronomy", "Herbology", "Defense Against the Dark Arts", "Divination", "Muggle Studies", "Ancient Runes", "History of Magic", "Transfiguration", "Potions", "Care of Magical Creatures", "Charms", "Flying"]

# loop all the separate histograms for each subject with the distributions per Hogwarts House
j = 6
k = 0
while j < number_of_columns:
	i = 0
	scores_R = []
	scores_H = []
	scores_G = []
	scores_S = []
	while i < number_of_rows:
		cell_content = input_file.iloc[i, j]
		if np.isnan(cell_content) == False:
			if input_file.iloc[i, 1] == "Ravenclaw":
				scores_R.append(cell_content)
			elif input_file.iloc[i, 1] == "Hufflepuff":
				scores_H.append(cell_content)
			elif input_file.iloc[i, 1] == "Gryffindor":
				scores_G.append(cell_content)
			elif input_file.iloc[i, 1] == "Slytherin":
				scores_S.append(cell_content)
		i += 1
	list_of_lists = [scores_R, scores_H, scores_G, scores_S]
	output = pd.DataFrame(list_of_lists)
	keys_list = ["Ravenclaw", "Hufflepuff", "Gryffindor", "Slytherin"]
	output.insert(0, " ", keys_list, True)
	plt.hist(scores_R, bins=10, label="Ravenclaw")
	plt.hist(scores_H, bins=10, label = "Hufflepuff")
	plt.hist(scores_G, bins=10, label = "Gryffindor")
	plt.hist(scores_S, bins=10, label = "Slytherin")
	plt.xlabel("Values")
	plt.ylabel("Frequency")
	plt.title("%s Scores" % (subjects[k]))
	plt.legend(loc='upper right')
	plt.show()
	j += 1
	k += 1

