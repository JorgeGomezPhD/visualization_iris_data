'''Write a Python program to find the correlation between variables of iris data. Also create a hitmap
 using Seaborn to present their relations.'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("iris.csv")
#Drop id column
# data = data.drop('species', axis=1)
X = data.iloc[:, 0:4]
f, ax = plt.subplots(figsize=(10, 8))
corr = X.corr()
print(corr)
sns.heatmap(corr, mask=np.zeros_like(corr, dtype=np.bool),
          cmap=sns.diverging_palette(220, 10, as_cmap=True),square=True, ax=ax, linewidths=.5)
plt.show()
