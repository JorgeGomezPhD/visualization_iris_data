'''Write a Python program to create a graph to find relationship between the sepal length and width.'''

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("iris.csv")
data[data.species == 'Iris-setosa'].plot(kind='scatter', x='sepal_length', y='sepal_width', color='orange', label='Setosa')
data[data.species == 'Iris-versicolor'].plot(kind='scatter', x='sepal_length', y='sepal_width', color='blue', label='versicolor')
data[data.species == 'Iris-virginica'].plot(kind='scatter', x='sepal_length', y='sepal_width', color='green', label='virginica')
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("Sepal Length VS Width")
plt.gcf()
# fig.set_size_inches(12,8)
plt.show()

