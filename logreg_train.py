import sys
from numpy.lib.function_base import gradient
import pandas as pd
import numpy as np

def sigmoid(x):
	return 1.0 / (1.0 * np.exp(-x))

def hypothesis(x, theta):
# do the matrix multiplication between x and theta
	return sigmoid(x.dot(theta))

def gradient(ys, xs, theta):
	g = np.zeros(len(xs[0]))
# len theta is the 14 subjects
	for j in range(len(theta)):
		g[j] = sum([(hypothesis(x, theta) - y) * x[j] for y, x in zip(ys, xs)]) / len(xs)
	return g

def gradient_descent(ys, xs, alpha, num_iter):
# returning a sample from a standard normal distribution
	thetas = np.random.randn(len(xs[0]))
# repeating the formula until convergence
# alpha is the step size [learning rate]
	for i in range(num_iter):
		thetas = thetas - alpha * gradient(ys, xs, thetas)
	return thetas

def train(ys, xs):
# thetas is the list with weights
	thetas = []
	for trained in np.unique(ys):
		ys_ally = ys.copy()
		ys_ally[ys == trained] = 0
		ys_ally[ys != trained] = 1
# trained is the index and the output of gradient_descent is the actual weight 
		thetas.append((trained, gradient_descent(ys_ally, xs, 1, 100)))
	return thetas

if __name__ == '__main__':
# input checking
	if len(sys.argv) != 2 :
		print ("Please provide an input file\n", end='')
		sys.exit(-1)
# reading input file from command line
	input_file = pd.read_csv(sys.argv[1])
# cleaning input file from Index column and nan values
	input_file.drop(columns=['Index'], inplace=True)
	input_file.dropna(axis=1, how="all", inplace=True)
	input_file.dropna(inplace=True)
# converting column titles into lowercase and replacing spaces with _
	input_file.columns = input_file.columns.str.lower()
	input_file.columns = input_file.columns.str.replace(' ', '_')
# create dataframe only with subject scores
	scores = input_file.loc[:, 'arithmancy':'flying']

# convert scores df to numpy array
	X = scores.values
# adding a column of ones in the vector, so that we can define the X*Theta in case the columns of our data matrics are less than the rows of matrix theta
	X = np.hstack([X, np.ones((X.shape[0], 1))])
# normalizing the data ; scaling all numeric variables in the range [0,1]
	X = (X - X.min()) / (X.max() - X.min())
# numpy array of houses - dependent variable
	Y = input_file["hogwarts_house"].values

	thetas = train(Y, X)
	with open("weights", "w") as file:
		for label, t in thetas:
			file.write("{}: {}\n".format(label, ','.join([str(x) for x in t])))
