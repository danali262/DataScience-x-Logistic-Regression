import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


if __name__ == "__main__":
    df = pd.read_csv("./datasets/dataset_train.csv")

    sns.pairplot(df, hue='Hogwarts House', diag_kind="hist")
    plt.show()
