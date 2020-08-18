'''Write a Python program to create a joinplot and add regression and kernel density fits using "reg"
to describe individual distributions on the same plot between Sepal length and Sepal width.'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("iris.csv")
sns.jointplot(x='sepal_length', y='sepal_width', kind="reg", color='red', data=data)
plt.show()