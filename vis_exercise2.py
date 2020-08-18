'''Write a Python program to create a Bar plot to get the frequency of the three species of the Iris data.'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("iris.csv")

plt.subplots(1,1,figsize=(10,8))
sns.countplot('species',data=data)
plt.title("Iris Species Count")
plt.show()

