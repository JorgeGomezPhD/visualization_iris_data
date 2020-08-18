'''Write a Python program to access first four cells from a given Dataframe using the index and column labels.
Call iris.csv to create the Dataframe.'''

import pandas as pd

data = pd.read_csv('iris.csv')

x = data.iloc[[1, 2, 3, 4]].values
print(x)
