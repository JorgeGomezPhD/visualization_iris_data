'''Write a Python program to load the iris data from a given csv fileinto a
dataframe and print the shape of the data, type of the data and first 3 rows.'''
import pandas as pd

#import data
data = pd.read_csv("iris.csv")
#data shape
print(data.shape)
#data type
print(type(data))
#print first 3 rows
print(data.head(3))