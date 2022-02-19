import pandas as pd


from srcs import user_input
from srcs import histogram_df as hdf


if __name__ == "__main__":
    df = pd.read_csv("./datasets/dataset_train.csv")
    print(type(df))

    # receive input from user for which subject to create histogram
    val = user_input.user_input()

    df_subject, subject = hdf.create_df(df, val)
    hdf.plot_histograms(df_subject, subject)
