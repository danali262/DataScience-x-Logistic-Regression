from os import terminal_size
import pandas as pd
import numpy as np
import sys
import csv

# input checking
if len(sys.argv) != 2 :
	print ("Please provide an input file\n", end='')
	sys.exit(-1)

# reading input file from command line
input_file = pd.read_csv(sys.argv[1])
columns_to_be_deleted = []
number_columns = len(input_file.columns)
i = 0

# creating a list of the columns to be deleted [ie the ones that use non-arithmetic data] and
# deleting these columns
while i < number_columns:
	row_content = input_file.iloc[0, i]
	if (type(row_content) == str):
		columns_to_be_deleted.append(i)
	i +=1
input_file.drop(input_file.columns[columns_to_be_deleted], axis=1, inplace=True)

