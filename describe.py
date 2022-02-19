import sys
import pandas as pd

from srcs import input
from srcs import clean_data as cd
from srcs import output


if __name__ == "__main__":
    # function to check the input
    input.check_input()

    # converting the input to a pandas dataframe object
    df = pd.read_csv(sys.argv[1])

    # data cleaning
    df_input = cd.clean_data(df)
    # print(df.describe())

    # create dataframe
    df_output = output.create_output(df_input)
    pd.set_option("display.max_rows", None, "display.max_columns", None)
    print(df_output)
