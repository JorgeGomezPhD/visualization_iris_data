'''Write a Python program to create a plot to get a general Statistics of Iris data.'''

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("iris.csv")
data.describe().plot(kind ="area", fontsize=16, figsize = (15, 8), table = True)
plt.ylabel('Value')
plt.title("Stats of Iris Dataset")
plt.show()