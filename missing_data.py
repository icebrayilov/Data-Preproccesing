# Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 2].values


# Taking care of missing data
# sklearn is library for preprocessing
# below code lines find missing values in first and second columns and replace them by mean of columns value.

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0) 
imputer = imputer.fit(X[:, 0:2]) 
X[:, 0:2] = imputer.transform(X[:, 0:2]) 
