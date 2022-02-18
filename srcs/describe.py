import input
import sys
import pandas as pd


if __name__ == "__main__":
    # function to check the input
    input.check_input()

    # converting the input to a pandas dataframe object
    df = pd.read_csv(sys.argv[1])
    print(df)