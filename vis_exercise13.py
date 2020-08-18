'''Write a Python program to create a pairplot of the iris data set and check which flower species
 seems to be the most separable.'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("iris.csv")
g = sns.jointplot(x="sepal_length", y="sepal_width", data=data, kind="kde", color="m")
g.plot_joint(plt.scatter, c="w", s=40, linewidth=1, marker="+")
g.ax_joint.collections[0].set_alpha(0)
g.set_axis_labels("$SepalLength(Cm)$", "$SepalWidth(Cm)$")
plt.show()