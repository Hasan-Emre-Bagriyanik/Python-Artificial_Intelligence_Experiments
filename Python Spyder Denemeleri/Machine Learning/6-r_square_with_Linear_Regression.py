# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 06:31:04 2023

@author: Hasan Emre
"""

#import library
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#import data
df = pd.read_csv("linear_regression_dataset.csv" , sep= ";")

#plot data
plt.scatter(df.deneyim, df.maas)
plt.ylabel("Maas")
plt.xlabel("Deneyim")
plt.show()

#%% linear regression

#sklearn library
from sklearn.linear_model import LinearRegression

#linear regression model
linear_reg = LinearRegression()

x = df.deneyim.values.reshape(-1,1)
y = df.maas.values.reshape(-1,1)

linear_reg.fit(x,y)
plt.scatter(x,y)
y_head = linear_reg.predict(x)

plt.plot(x,y_head, color = "red")


#%% r_square hesaplama yapacagız

from sklearn.metrics import r2_score

print("r_square score: ", r2_score(y, y_head))




