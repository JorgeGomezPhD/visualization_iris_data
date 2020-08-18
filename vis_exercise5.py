'''Write a Python program to create a graph to find relationship between the petal length and width.'''

import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("iris.csv")
fig = data[data.species == 'Iris-setosa'].plot.scatter(x='sepal_length', y='petal_width', color='orange', label='Setosa')
data[data.species == 'Iris-versicolor'].plot.scatter(x='sepal_length', y='petal_width', color='blue', label='versicolor', ax=fig)
data[data.species == 'Iris-virginica'].plot.scatter(x='sepal_length', y='petal_width', color='green', label='virginica', ax=fig)
fig.set_xlabel("Petal Length")
fig.set_ylabel("Petal Width")
fig.set_title(" Petal Length VS Width")
fig=plt.gcf()
fig.set_size_inches(12,8)
plt.show()