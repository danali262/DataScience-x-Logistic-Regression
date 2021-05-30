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

# create lists with the scores of each subject
i = 0
arithmancy_scores = []
astronomy_scores = []
herbology_scores = []
defense_scores = []
divination_scores = []
muggle_scores = []
runes_scores = []
history_scores = []
transfig_scores = []
potions_scores = []
care_scores = []
charms_scores = []
flying_scores = []
while i < number_of_rows:
	cell_content = input_file.iloc[i, 6]
	# if np.isnan(cell_content) == False:
	arithmancy_scores.append(cell_content)
	cell_content = input_file.iloc[i, 7]
	# if np.isnan(cell_content) == False:
	astronomy_scores.append(cell_content)
	cell_content = input_file.iloc[i, 8]
	# if np.isnan(cell_content) == False:
	herbology_scores.append(cell_content)
	cell_content = input_file.iloc[i, 9]
	# if np.isnan(cell_content) == False:
	defense_scores.append(cell_content)
	cell_content = input_file.iloc[i, 10]
	# if np.isnan(cell_content) == False:
	divination_scores.append(cell_content)
	cell_content = input_file.iloc[i, 11]
	# if np.isnan(cell_content) == False:
	muggle_scores.append(cell_content)
	cell_content = input_file.iloc[i, 12]
	# if np.isnan(cell_content) == False:
	runes_scores.append(cell_content)
	cell_content = input_file.iloc[i, 13]
	# if np.isnan(cell_content) == False:
	history_scores.append(cell_content)
	cell_content = input_file.iloc[i, 14]
	# if np.isnan(cell_content) == False:
	transfig_scores.append(cell_content)
	cell_content = input_file.iloc[i, 15]
	# if np.isnan(cell_content) == False:
	potions_scores.append(cell_content)
	cell_content = input_file.iloc[i, 16]
	# if np.isnan(cell_content) == False:
	care_scores.append(cell_content)
	cell_content = input_file.iloc[i, 17]
	# if np.isnan(cell_content) == False:
	charms_scores.append(cell_content)
	cell_content = input_file.iloc[i, 18]
	# if np.isnan(cell_content) == False:
	flying_scores.append(cell_content)
	i += 1

list_of_lists = [arithmancy_scores, astronomy_scores, herbology_scores, defense_scores, divination_scores, muggle_scores, runes_scores, history_scores, transfig_scores, potions_scores, care_scores, charms_scores, flying_scores]
subjects = ["Arithmancy", "Astronomy", "Herbology", "Defense Against the Dark Arts", "Divination", "Muggle Studies", "Ancient Runes", "History of Magic", "Transfiguration", "Potions", "Care of Magical Creatures", "Charms", "Flying"]

# i = 0
# while i < 13:
# 	j = i + 1
# 	while j < 12:
# 		plt.scatter(list_of_lists[i], list_of_lists[j])
# 		plt.xlabel("%s" % (subjects[i]))
# 		plt.ylabel("%s" % (subjects[j]))
# 		plt.show()
# 		j += 1
# 	i += 1

# show the requested scatter plot
plt.scatter(defense_scores, astronomy_scores)
plt.xlabel("Defense Against the Dark Arts")
plt.ylabel("Astronomy")
plt.show()