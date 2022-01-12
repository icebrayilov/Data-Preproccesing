# Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
# Import all lines values, except last columns.(independent valuables)
X = dataset.iloc[:, :-1].values
# Import dependent values 
y = dataset.iloc[:, 2].values

# Splitting the dataset into the Training set and Test set
# test_size define that 20% is of values are splitted for test values of machine learning, other values for train values.
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
