# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 09:30:14 2023

@author: Hasan Emre
"""


import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("polynomial_regression.csv", sep=";")
 
y = df.araba_max_hiz.values.reshape(-1,1)
x = df.araba_fiyat.values.reshape(-1,1)


plt.scatter(x,y)
plt.xlabel("Araba  max fiyat")
plt.ylabel("Araba fiyatı")
plt.show()


# linear regression   y = b0 + b1*x
# multiple linear regression  y = b0 + b1*x + b2*x2

#%% linear regression 
from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(x,y)


#%% predict

y_head = lr.predict(x)
plt.scatter(x, y)
plt.plot(x,y_head, color = "red")
plt.show()

lr.predict([[10000]])


#%%
# polynomial regression =  y = b0 + b1*x +b2*x^2 + b3*x^3 + ... + bn*x^n

from sklearn.preprocessing import PolynomialFeatures
polynomial_regression = PolynomialFeatures(degree=2)

x_polynomial = polynomial_regression.fit_transform(x)

# fit

linear_regression2 = LinearRegression()
linear_regression2.fit(x_polynomial, y)

y_head2 = linear_regression2.predict(x_polynomial)
plt.scatter(x, y)
plt.plot(x,y_head2, color = "black" ,label = "poly")
plt.legend()
plt.show()


#%%  
# ploinomun derecesi yukseldikce line dogrulugu artar

from sklearn.preprocessing import PolynomialFeatures
polynomial_regression = PolynomialFeatures(degree=4)

x_polynomial = polynomial_regression.fit_transform(x)

# fit

linear_regression2 = LinearRegression()
linear_regression2.fit(x_polynomial, y)

y_head2 = linear_regression2.predict(x_polynomial)
plt.scatter(x, y)
plt.plot(x,y_head2, color = "black" ,label = "poly")
plt.legend()
plt.show()






