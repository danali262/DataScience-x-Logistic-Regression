import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score
from csv import writer
from csv import reader


from srcs import methods_describe


def clean_df(df):
    output_df = df.drop(['Index', 'Hogwarts House', 'First Name', 'Last Name', 'Birthday', 'Best Hand'], axis=1)

    count_list, min_list, max_list, mean_list, first_quartile_list, second_quartile_list, third_quartile_list = \
        methods_describe.create_lists(output_df)

    i = 0
    for (colname, colvalue) in output_df.iteritems():
        output_df[colname] = output_df[colname].fillna(mean_list[i])
        i += 1

    return output_df


def add_column_in_csv(input_file, output_file, transform_row):
    with open(input_file, 'r') as read_obj, \
            open(output_file, 'w', newline='') as write_obj:
        csv_reader = reader(read_obj)
        csv_writer = writer(write_obj)
        for row in csv_reader:
            transform_row(row, csv_reader.line_num)
            csv_writer.writerow(row)


if __name__ == "__main__":
    df = pd.read_csv("./datasets/dataset_train.csv")
    df_test = pd.read_csv("./datasets/dataset_test.csv")

    # Remove non-arithmetic columns [apart from Hogwarts House] and replace NaNs with mean of each column
    new_df = clean_df(df)
    new_df_test = clean_df(df_test)

    # dependent value is Hogwarts House
    y = df['Hogwarts House']
    # we are dropping Astronomy and Defense Against the Dark Arts, which are inversely proportional
    X = new_df.drop(['Astronomy', 'Defense Against the Dark Arts'], axis=1)

    # scaling the data
    scaler = MinMaxScaler()
    X = scaler.fit_transform(X)

    # splitting the train set to 20% test set, 80% train set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

    # running the Regression and fitting to Linear Model
    regressor = LogisticRegression()
    regressor.fit(X_train, y_train)

    # predict using the linear model
    y_pred = regressor.predict(X_test)

    # calculating the accuracy score based on our training set
    acc_score = accuracy_score(y_test, y_pred)
    # print("Accuracy is: ", acc_score)

    # Apply the regressor to the test dataset to predict the Hogwarts House
    X_test = new_df_test.drop(['Astronomy', 'Defense Against the Dark Arts'], axis=1)
    X_test = scaler.fit_transform(X_test)

    # y_pred here is the predicted Hogwarts Houses for the test set
    y_pred = regressor.predict(X_test)

    df_test["Hogwarts House"] = list(y_pred)
    df_test.to_csv("./datasets/regression_output.csv", index=False)
