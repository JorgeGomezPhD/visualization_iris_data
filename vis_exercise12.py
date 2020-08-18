'''Write a Python program to create a joinplot using "kde" to describe individual distributions on the
same plot between Sepal length and Sepal width and use '+' sign as marker. Note: The kernel
density estimation (kde) procedure visualize a bivariate distribution. In seaborn, this kind of plot is
shown with a contour plot and is available as a style in jointplot().'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("iris.csv")
g = sns.jointplot(x="sepal_length", y="sepal_width", data=data, kind="kde", color="m")
g.plot_joint(plt.scatter, c="w", s=40, linewidth=1, marker="+")
g.ax_joint.collections[0].set_alpha(0)
g.set_axis_labels("$SepalLength(Cm)$", "$SepalWidth(Cm)$")
plt.show()