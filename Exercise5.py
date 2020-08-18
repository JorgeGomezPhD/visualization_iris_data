'''Write a Python program to view basic statistical details like percentile, mean, std etc. of iris data.'''

import pandas as pd

data = pd.read_csv('iris.csv')
print(data.describe())
