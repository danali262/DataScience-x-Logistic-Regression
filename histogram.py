import pandas as pd


from srcs import user_input
from srcs import methods_visualization as vis


if __name__ == "__main__":
    df = pd.read_csv("./datasets/dataset_train.csv")

    # receive input from user for which subject to create histogram
    val = user_input.user_input_histogram()

    df_subject, subject = vis.create_df(df, val)
    vis.plot_histograms(df_subject, subject)
