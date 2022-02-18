import math


def fill_count(df_input):
    result = []

    for (colname, colval) in df_input.iteritems():
        values_list = colval.values
        clear_values_list = [x for x in values_list if math.isnan(x) == False]
        result.append(len(clear_values_list))

    return result


def fill_mean(df_input, count_list):
    sum_list = []

    for (colname, colval) in df_input.iteritems():
        values_list = colval.values
        clear_values_list = [x for x in values_list if math.isnan(x) == False]
        sum = 0
        for x in clear_values_list:
            sum = sum + x
        sum_list.append(sum)

    result = [i / j for i, j in zip(sum_list, count_list)]

    return result
