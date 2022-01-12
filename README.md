# Data-Preproccesing
Data Preprocessing for Data Science

For Data usage in Data Science projects, firstly needed to organize and preprocess data.

In given Data file we have Age, Salary columns as independent values and Product Purchased? column as dependent values.
There is missing values in Age and Salary columns. 
With missing_data.py python codes we detect and replace missing_data with mean value of Age and Salary columns' values.

Product Purchased columns contains 'Yes' and 'No' values as category. Because other columns values are integer, we need to encode categorical data to integer as '0'/'1'

After missing_data replaced and categorical data is encoded, we split our datas to train and test sets for machine learning in test_train_split.py.

In all code files, there is detailed information about code lines.
