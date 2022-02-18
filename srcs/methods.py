import math


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
        sorted_values_list = sorted(clear_values_list)

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

    return count_list, min_list, max_list, mean_list

# def fill_std(df_input, mean_list):
#     sq_diff_list = []
#
#     for (colname, colval) in df_input.iteritems():
#         values_list = colval.values
#         clear_values_list = [x for x in values_list if math.isnan(x) == False]
#         for x in clear_values_list:
#             diff = x - mean
#             sq_diff = diff ** 2

def fill_quartile(df_input, count_list):
    first_quartile_list = []
    second_quartile_list = []
    third_quartile_list = []

    # Counter to easily correspond the count list items with the corresponding column
    i_col = 0
    for (colname, colval) in df_input.iteritems():
        # values_list = colval.values
        # clear_values_list = [x for x in values_list if math.isnan(x) == False]
        # clear_values_list.sort()
        i_col += 1

