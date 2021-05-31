import pandas as pd
import numpy as np
import sys
import seaborn as sns
import matplotlib.pyplot as plt

# input checking
if len(sys.argv) != 2 :
	print ("Please provide an input file\n", end='')
	sys.exit(-1)

# reading input file from command line
input_file = pd.read_csv(sys.argv[1])
number_of_rows = len(input_file)
number_of_columns = len(input_file.columns)
subjects = ["Arithmancy", "Astronomy", "Herbology", "Defense Against the Dark Arts", "Divination", "Muggle Studies", "Ancient Runes", "History of Magic", "Transfiguration", "Potions", "Care of Magical Creatures", "Charms", "Flying"]

# create default pairplot
sns.pairplot(input_file, hue='Hogwarts House')
plt.show()

