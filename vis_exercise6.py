'''Write a Python program to create a graph to see how the length and
width of SepalLength, SepalWidth, PetalLength, PetalWidth are distributed.'''

import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("iris.csv")
# Drop id column
new_data = data.drop('species', axis=1)
new_data.hist(edgecolor='black', linewidth=1.2)
plt.gcf()
plt.show()