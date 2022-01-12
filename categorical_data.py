# Data Preprocessing

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')
y = dataset.iloc[:, 2].values


# Encoding categorical data
# Encoding the Dependent Variable 
# Dependent variable is string. To encode string we use LabelEncoder class. Below lines change 'Yes'/'No' string to '0'/'1'
from sklearn.preprocessing import LabelEncoder,
labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)
