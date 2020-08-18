'''Write a Python program to draw a scatterplot, then add a joint density estimate to describe
individual distributions on the same plot between Sepal length and Sepal width.'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("iris.csv")
sns.jointplot("sepal_length", "sepal_width", data=data, color="blue").plot_joint(sns.kdeplot, zorder=0, n_levels=6)
plt.show()