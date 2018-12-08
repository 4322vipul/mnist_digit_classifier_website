# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset=pd.read_csv("data.csv")
x=dataset.iloc[:,1:2].values
y=dataset.iloc[:,2].values

#Fitting the decision tree model regression to the data set
from sklearn.tree import DecisionTreeRegressor
regressor=DecisionTreeRegressor(random_state=0)
regressor.fit(x,y)

#Visualising the plot of tree regression
#for higher resolution
x_grid=np.arange(min(x),max(x),0.01)
x_grid=x_grid.reshape((len(x_grid),1))

plt.scatter(x,y,color='red')
plt.plot(x_grid,regressor.predict(x_grid),color='blue')
plt.title('Decision tree model plot')
plt.xlabel('post')
plt.ylabel('Salaries')
plt.show()

#predicting the value of y using the tree regression
y_pred=regressor.predict(5)

