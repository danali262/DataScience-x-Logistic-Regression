import numpy as np
import pandas as pd


from srcs import clean_data as cd
from srcs import user_input
from srcs import histogram_df as hdf


if __name__ == "__main__":
    df = pd.read_csv("./datasets/dataset_train.csv")

    # receive input from user for which subject to create histogram
    val = user_input.user_input()

    df_subject = hdf.create_df(df, val)
