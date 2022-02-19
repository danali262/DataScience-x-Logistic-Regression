import pandas_profiling as pp
import sys

# even though the use of Pandas' describe method is not allowed to produce the final output,
# we run Pandas Profiling on our dataset to guide us on how to clean our data efficiently


def pandas_profiling(df):
    profile = pp.ProfileReport(df)

    # convert the report to an HTML file for easy readability from our browser
    profile.to_file("Report.html")


def clean_data(df):
    # uncomment to run
    # pandas_profiling(df)

    # we need to remove all non-numerical columns
    df_clean = df.select_dtypes(include='number')

    if df_clean.empty:
        print("Input dataset contains only non-numerical values.")
        sys.exit(-1)

    # running pandas_profiling again on the clean set for sanity check - uncomment to run
    # pandas_profiling(df_clean)

    return df_clean
