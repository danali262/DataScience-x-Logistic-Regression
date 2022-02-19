import pandas as pd


from srcs import user_input
from srcs import methods_visualization as vis


if __name__ == "__main__":
    df = pd.read_csv("./datasets/dataset_train.csv")

    # receive input from user for which subjects to create scatter plot
    val1, val2 = user_input.user_input_scatterplot()

    df_subject1, subject1 = vis.create_df(df, val1)
    df_subject2, subject2 = vis.create_df(df, val2)
    vis.plot_scatter(df_subject1, subject1, df_subject2, subject2)
