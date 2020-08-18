'''Write a Python program to create a joinplot using "hexbin" to describe individual distributions on
the same plot between Sepal length and Sepal width. Note: The bivariate analogue of a histogram
is known as a "hexbin" plot, because it shows the counts of observations that fall within hexagonal
bins. This plot works best with relatively large datasets. It's available through the matplotlib
plt.hexbin function and as a style in jointplot(). It looks best with a white background.'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("iris.csv")
sns.jointplot(x='sepal_length', y='sepal_width', kind="hex", color="red", data=data)
plt.show()