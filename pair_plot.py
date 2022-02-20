import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt


if __name__ == "__main__":
    df = pd.read_csv("./datasets/dataset_train.csv")

    new_df = df.drop(columns=['Index', 'First Name', 'Last Name', 'Birthday', 'Best Hand'])
    sns.set_context("paper", rc={"axes.labelsize":5})
    g = sns.pairplot(new_df, hue='Hogwarts House', diag_kind="hist", height=1)
    g.set(xticklabels=[], yticklabels=[])
    plt.show()
