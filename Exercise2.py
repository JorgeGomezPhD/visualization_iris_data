'''Write a Python program using Scikit-learn to print the keys, number of rows-columns,
feature names and the description of the Iris data'''
#import and define data
import pandas as pd
data = pd.read_csv('iris.csv')
#print keys
print(f'Iris data keys:\n{data.keys()}')
#print number of rows-columns
print(f'Number of rows and columns:\n{data.shape}')
