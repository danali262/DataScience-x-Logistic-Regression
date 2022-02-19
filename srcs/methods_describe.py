import math
import numpy as np

# Globals for quartile computation
FIRST_QUARTILE = 25
SECOND_QUARTILE = 50
THIRD_QUARTILE = 75


def clean_values(colnmame, colval):
    values_list = colval.values
    clear_values_list = [x for x in values_list if math.isnan(x) == False]

    return clear_values_list


def calculate_min_max_sum(x, min, max, sum):
    if x < min:
        min = x
    if x > max:
        max = x
    sum = sum + x

    return min, max, sum


def calculate_percentiles(input_list, clear_values_list, p):
    sorted_values_list = sorted(clear_values_list)
    data_point = (len(sorted_values_list) - 1) * (p / 100)

    floor = np.floor(data_point)
    ceiling = np.ceil(data_point)

    if floor == ceiling:
        input_list.append(sorted_values_list[int(data_point)])
        return input_list

    d0 = sorted_values_list[int(floor)] * (ceiling - data_point)
    d1 = sorted_values_list[int(ceiling)] * (data_point - floor)
    input_list.append(d0 + d1)

    return input_list


def create_lists(df_input):
    count_list = []
    min_list = []
    max_list = []
    sum_list = []
    mean_list = []
    first_quartile_list = []
    second_quartile_list = []
    third_quartile_list = []

    # loop going through input_dataframe columns and column_values and creating lists with the metrics we need
    for (colname, colval) in df_input.iteritems():
        clear_values_list = clean_values(colname, colval)

        first_quartile_list = calculate_percentiles(first_quartile_list, clear_values_list, FIRST_QUARTILE)
        second_quartile_list = calculate_percentiles(second_quartile_list, clear_values_list, SECOND_QUARTILE)
        third_quartile_list = calculate_percentiles(third_quartile_list, clear_values_list, THIRD_QUARTILE)

        count_list.append(len(clear_values_list))

        min = clear_values_list[0]
        max = clear_values_list[0]
        sum = 0

        for x in clear_values_list:
            min, max, sum = calculate_min_max_sum(x, min, max, sum)
        min_list.append(min)
        max_list.append(max)
        sum_list.append(sum)

    mean_list = [i / j for i, j in zip(sum_list, count_list)]

    return count_list, min_list, max_list, mean_list, first_quartile_list, second_quartile_list, third_quartile_list


def fill_std(df_input, mean_list, count_list):
    sq_diff_list = []
    mean_sq_diff_list = []
    std_dev_list = []

    # Counter to easily correspond the mean list items with the corresponding column
    i_col = 0
    for (colname, colval) in df_input.iteritems():
        clear_values_list = clean_values(colname, colval)
        sum_sq_diff = 0
        for x in clear_values_list:
            diff = x - mean_list[i_col]
            sq_diff = diff ** 2
            sum_sq_diff = sum_sq_diff + sq_diff
        sq_diff_list.append(sum_sq_diff)
        i_col += 1

    mean_sq_diff_list = [i / j for i, j in zip(sq_diff_list, count_list)]
    std_dev_list = np.sqrt(mean_sq_diff_list)

    return std_dev_list
