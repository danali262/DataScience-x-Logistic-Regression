from enum import Enum
import math
import matplotlib.pyplot as plt


class Subject(Enum):
    Arithmancy = 1
    Astronomy = 2
    Herbology = 3
    Defense_Against_the_Dark_Arts = 4
    Divination = 5
    Muggle_Studies = 6
    Ancient_Runes = 7
    History_of_Magic = 8
    Transfiguration = 9
    Potions = 10
    Care_of_Magical_Creatures = 11
    Charms = 12
    Flying = 13


def create_df(input_df, val):
    subject = Subject(val).name
    new_subject = subject.replace('_', ' ')

    output_df = input_df[["Hogwarts House", new_subject]].copy()

    return output_df, new_subject


def plot_histograms(df, subject):
    Gryffindor_scores = []
    Slytherin_scores = []
    Ravenclaw_scores = []
    Hufflepuff_scores = []

    for ind in df.index:
        if not df['Hogwarts House'][ind] or math.isnan(df[subject][ind]):
            continue
        if df['Hogwarts House'][ind] == 'Gryffindor':
            Gryffindor_scores.append(df[subject][ind])
        elif df['Hogwarts House'][ind] == 'Slytherin':
            Slytherin_scores.append(df[subject][ind])
        elif df['Hogwarts House'][ind] == 'Ravenclaw':
            Ravenclaw_scores.append(df[subject][ind])
        else:
            Hufflepuff_scores.append(df[subject][ind])

    plt.hist(Gryffindor_scores, color='red', alpha=0.5)
    plt.hist(Slytherin_scores, color='green', alpha=0.5)
    plt.hist(Ravenclaw_scores, color='blue', alpha=0.5)
    plt.hist(Hufflepuff_scores, color='yellow', alpha=0.5)

    legend = ['Gryffindor', 'Slytherin', 'Ravenclaw', 'Hufflepuff']
    plt.legend(legend, loc="upper right", frameon=False)
    plt.title(subject)
    plt.xlabel('Marks')
    plt.ylabel('Number of students')
    plt.show()
