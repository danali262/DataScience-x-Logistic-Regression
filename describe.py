from os import terminal_size
import pandas as pd
import numpy as np
import sys
import csv
import math

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
number_columns = len(input_file.columns)
# print(input_file)

# creating a panda dataframe from scratch using list of lists. Every row of the data frame is 
# a list.
keys_list = [" ", "Count", "Mean", "Std", "Min", "25%", "50%", "75%", "Max"]
features_list = []
count_list = []
mean_list = []
std_list = []
min_list = []
twentyfiveper_list = []
fiftyper_list = []
seventyfiveper_list = []
max_list = []

# build features_list
i = 0
while i < number_columns:
	feature = input_file.columns[i]
	features_list.append(feature)
	i += 1
# print (features_list)

# build count_list
j = 0
number_of_rows = len(input_file)
while j < number_columns:
	count = 0
	i = 0
	while i < number_of_rows:
		cell_content = input_file.iloc[i, j]
		if np.isnan(cell_content) == False:
			count += 1
		i += 1
	count_list.append(format(count, '.5f'))
	j += 1
# print(count_list)

# build mean_list
j = 0
while j < number_columns:
	i = 0
	sum = 0
	mean = 0
	while i < number_of_rows:
		cell_content = input_file.iloc[i, j]
		if np.isnan(cell_content) == False:
			sum = sum + cell_content
			mean = (sum * 1.0) / float(count_list[j])
		i += 1
	mean_list.append(format(float(mean), '.6f'))
	j += 1
# print(mean_list)

# build std_list
j = 0
while j < number_columns:
	i = 0
	sum_square_diff = 0
	square_diff = 0
	mean_square_diff = 0
	std = 0
	while i < number_of_rows:
		cell_content = input_file.iloc[i, j]
		if np.isnan(cell_content) == False:
			square_diff = (cell_content - float(mean_list[j])) ** 2
			sum_square_diff = sum_square_diff + square_diff
			mean_square_diff = (sum_square_diff * 1.0) / float(count_list[j])
			std = math.sqrt(mean_square_diff)
		i += 1
	std_list.append(format(float(std), '.6f'))
	j += 1
# print(std_list)

# build min_list
j = 0
while j < number_columns:
	i = 0
	min = input_file.iloc[i, j]
	while i < number_of_rows:
		cell_content = input_file.iloc[i, j]
		if cell_content < min:
			min = cell_content
		i += 1
	min_list.append(format(float(min), '.6f'))
	j += 1
# print(min_list)

# build max_list
j = 0
while j < number_columns:
	i = 0
	max = input_file.iloc[i, j]
	while i < number_of_rows:
		cell_content = input_file.iloc[i, j]
		if cell_content > max:
			max = cell_content
		i += 1
	max_list.append(format(float(max), '.6f'))
	j += 1
# print(max_list)

list_of_lists = [keys_list, features_list, count_list, mean_list, std_list, min_list, max_list]
output_file = pd.DataFrame(list_of_lists)
print(output_file)

print("describe gives us")
print(input_file.describe())