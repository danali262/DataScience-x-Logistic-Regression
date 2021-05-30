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

# creating a panda dataframe from scratch using list of lists. Every row of the data frame is 
# a list. The keys_list is the first column.
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
	count_list.append(format(count, '.6f'))
	j += 1

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

# build twentyfiveper_list
j = 0
while j < number_columns:
	i = 0
	values = []
	per = 0.25
	index = 0
	while i < number_of_rows:
		cell_content = input_file.iloc[i, j]
		if np.isnan(cell_content) == False:
			values.append(cell_content)
		i += 1
	values.sort()
	index = per * float(count_list[j])
	if index.is_integer():
		twentyfiveper = values[int(index)]
	else:
		twentyfiveper = values[int(math.ceil(index)) - 1]
	twentyfiveper_list.append(format(float(twentyfiveper), '.6f'))
	j += 1

# build fiftyper_list
j = 0
while j < number_columns:
	i = 0
	values = []
	per = 0.50
	index = 0
	while i < number_of_rows:
		cell_content = input_file.iloc[i, j]
		if np.isnan(cell_content) == False:
			values.append(cell_content)
		i += 1
	values.sort()
	index = per * float(count_list[j])
	if index.is_integer():
		fiftyper = values[int(index)]
	else:
		fiftyper = values[int(math.ceil(index)) - 1]
	fiftyper_list.append(format(float(fiftyper), '.6f'))
	j += 1

# build seventyfiveper_list
j = 0
while j < number_columns:
	i = 0
	values = []
	per = 0.75
	index = 0
	while i < number_of_rows:
		cell_content = input_file.iloc[i, j]
		if np.isnan(cell_content) == False:
			values.append(cell_content)
		i += 1
	values.sort()
	index = per * float(count_list[j])
	if index.is_integer():
		seventyfiveper = values[int(index)]
	else:
		seventyfiveper = values[int(math.ceil(index)) - 1]
	seventyfiveper_list.append(format(float(seventyfiveper), '.6f'))
	j += 1 

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

list_of_lists = [features_list, count_list, mean_list, std_list, min_list, twentyfiveper_list, fiftyper_list, seventyfiveper_list, max_list]
output_file = pd.DataFrame(list_of_lists)
keys_list = [" ", "count", "mean", "std", "min", "25%", "50%", "75%", "max"]
output_file.insert(0, " ", keys_list, True)
# output_file.to_csv('describe.csv')
print(output_file)
