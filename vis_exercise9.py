'''Write a Python program to create a joinplot using "kde" to describe individual distributions on
the same plot between Sepal length and Sepal width. Note: The kernel density estimation (kde)
procedure visualize a bivariate distribution. In seaborn, this kind of plot is shown with a contour
plot and is available as a style in jointplot().'''

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
data = pd.read_csv("iris.csv")
sns.jointplot(x='sepal_length', y='sepal_width', kind="kde", color='cyan', data=data)
plt.show()