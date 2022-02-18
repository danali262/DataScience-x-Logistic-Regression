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
    count_list = methods.fill_count(df_input)
    df_output.loc["Count"] = count_list

    df_output.loc["Mean"] = methods.fill_mean(df_input, count_list)
    # df_output.loc["Std"] = methods.fill_std(df_input)
    # df_output.loc["Min"] = methods.fill_min(df_input)
    # df_output.loc["25%"] = methods.fill_first_quartile(df_input)
    # df_output.loc["50%"] = methods.fill_second_quartile(df_input)
    # df_output.loc["75%"] = methods.fill_third_quartile(df_input)
    # df_output.loc["Max"] = methods.fill_max(df_input)

    return df_output


def create_output(df_input):
    df_output = create_dataframe(df_input)
    df_output = fill_values(df_output, df_input)
    print(df_output)