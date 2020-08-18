'''Write a Python program to create a box plot (or box-and-whisker plot) which shows the distribution
of quantitative data in a way that facilitates comparisons between variables or across levels of a
categorical variable of iris dataset. Use seaborn.'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("iris.csv")
#Drop id column
# data = data.drop('Id', axis=1)
box_data = data #variable representing the data array
box_target = data.species #variable representing the labels array
sns.boxplot(data = box_data,width=0.5,fliersize=5)
sns.set(rc={'figure.figsize':(2,15)})
plt.show()