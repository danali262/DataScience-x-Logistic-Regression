from enum import Enum


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
    # print(new_subject)

    # output_df = input_df.drop(input_df.columns.difference(['Hogwarts House', new_subject]), 1, inplace=True)
    output_df = input_df[["Hogwarts House", new_subject]]
    print(output_df)

    