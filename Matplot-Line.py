#Download dataset from here : https://archive.ics.uci.edu/ml/machine-learning-databases/iris/ #Iris.data
#Rename that to iris.csv
#Data Visualization with MatPlotLib
#Reading the data
import pandas as pd
import matplotlib.pyplot as plt
iris = pd.read_csv('iris.csv', names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class'])


##LINE CHART
columns = iris.columns.drop(['class'])
x_data = range(0, iris.shape[0])
fig, ax = plt.subplots()
for column in columns:
    ax.plot(x_data, iris[column], label=column)
ax.set_title('Iris Dataset')
ax.legend()





