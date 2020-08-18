'''Write a Python program to create a joinplot to describe individual distributions on the same plot
between Sepal length and Sepal width. Note: joinplot - Draw a plot of two variables with bivariate
 and univariate graphs.'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("iris.csv")
sns.jointplot(x='sepal_length', y='sepal_width', data=data, color='blue')
plt.show()