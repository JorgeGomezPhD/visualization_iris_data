'''Write a Python program to get the number of observations, missing values and nan values'''
import pandas as pd

data = pd.read_csv("iris.csv")
print(data.info())