'''Write a Python program using seaborn to Create a kde (Kernel Density Estimate ) plot of
sepal_length versus sepal width for setosa species of flower.'''

# Import necessary modules
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv("iris.csv")
#Drop id column
# data = data.drop('Id', axis=1)
sub=data[data['species'] == 'Iris-setosa']
sns.kdeplot(data=sub[['sepal_length','sepal_width']],cmap="plasma", shade=True, shade_lowest=False)
plt.title('Iris-setosa')
plt.xlabel('Sepal Length cm')
plt.ylabel('Sepal Width cm')
plt.show()