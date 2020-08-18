'''Write a Python program using seaborn to Create a kde (Kernel Density Estimate ) plot of
petal_length versus petal width for setosa species of flower.'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("iris.csv")
#Drop id column
# data = data.drop('Id', axis=1)
sub=data[data['species'] == 'Iris-setosa']
sns.kdeplot(data=sub[['petal_length','petal_width']],cmap="plasma", shade=True, shade_lowest=False)
plt.title('Iris-setosa')
plt.xlabel('Petal Length Cm')
plt.ylabel('Petal Width Cm')
plt.show()