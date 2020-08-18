'''Write a Python program to drop Id column from a given Dataframe and print the modified part. 
Call iris.csv to create the Dataframe.'''

import pandas as pd

data = pd.read_csv('iris.csv')
print('Originla data with no modifications: ')
print(data.head())

data_drop = data.drop('sepal_width',axis=1)
print('New data with dropped column:')
print(data_drop.head())