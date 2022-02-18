import pandas as pd
import methods


# Creates an empty dataframe with column names & row indices but no data
def create_dataframe(df_input):
    features_list = list(df_input.columns.values)
    metrics_list = ["Count", "Mean", "Std", "Min", "25%", "50%", "75%", "Max"]

    df_output = pd.DataFrame(columns=features_list, index=metrics_list)
    # print(df_output)

    return df_output


def fill_values(df_output, df_input):
    count_list, min_list, max_list, mean_list = methods.create_lists(df_input)

    df_output.loc["Count"] = count_list
    df_output.loc["Min"] = min_list
    df_output.loc["Max"] = max_list
    df_output.loc["Mean"] = mean_list

    # Calculate std deviation
    # df_output.loc["Std"] = methods.fill_std(df_input, mean_list)

    # Calculate percentiles
    # first_quartile_list, second_quartile_list, third_quartile_list = methods.fill_quartile(df_input, count_list)
    # df_output.loc["25%"] = first_quartile_list
    # df_output.loc["50%"] = second_quartile_list
    # df_output.loc["75%"] = third_quartile_list

    return df_output


def create_output(df_input):
    df_output = create_dataframe(df_input)
    df_output = fill_values(df_output, df_input)
    print(df_output)
