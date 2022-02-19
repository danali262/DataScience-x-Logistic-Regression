# Data Science x Logistic Regression

The aim of that project is to create a classifier that reproduces the behaviour of Hogwards' Sorting Hat.

There are three parts of the project:

1. <strong>Data Analysis</strong>
2. <strong>Data Visualization</strong>
3. <strong>Logistic Regression</strong>

## Installation

Run `make install`

## Data Analysis

In the <strong>Data Analysis</strong> part the aim is to produce a `describe.py` program, which mimics the behaviour of `pandas.DataFrame.describe` method.

The use of `describe`, `count`, `mean`, `std`, `min`, `max`, `percentile` functions is <strong>forbidden</strong>. 

> Usage

```python3
describe.py [dataset_path]
```

> Example


![describe_example](/images/describe_example.png)

## Data Visualization

In the <strong>Data Visualization</strong> part the aim is to create a <strong>histogram</strong>, a <strong>scatter plot</strong>, and a <strong>pair plot</strong> of our training dataset.

### Histogram

The histogram allows the user to see the distribution of scores across the four Hogwarts Houses per subject. The user is asked to provide the index of the subject which histogram they need and therafter the program produces the histogram.

> Usage

```python3
histogram.py
```

> Example

// add screenshot

### Scatter Plot

The scatter plot allows the user to see the relationship of the distibution of scores of two subjects across the four Hogwarts Houses. The user is asked to provide the indices of the two subjects to be compares and thereafter the program produces the scatter plot.

> Usage

```python3
scatter_plot.py
```

> Example

// add screenshot

### Pair plot

The pair plot creates a scatter plot matrix comparing all subjects in pairs of two across the four Hogwarts Houses. No user input is required.

> Usage

```python3
pair_plot.py
```

> Example

// add screenshot

