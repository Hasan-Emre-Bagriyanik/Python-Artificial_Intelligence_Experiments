# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 08:19:37 2023

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

 #%% prediction (Tahmin)

b0 = linear_reg.predict([[0]])   # y = b0 + b1.x   predict fonksiyonu ile x yerine sifir yazarak b0 degerini buluyor
print("b0: ",b0)

b0_ = linear_reg.intercept_      # y ekseninde kesistigi yer b0 degeridir.  Bu da farkli yoldan b0 i bulma 
print("b0_: ", b0_)

b1 = linear_reg.coef_  # coef = coefficient (katsayi)
print("b1: ",b1)       # slope (egim)

# maas = 1663 + 1138*deneyim

maas_yeni  = 1663 + 1138*11  # denkleme buldugumuz degerleri yazarak maaslari bulabiliriz.
print(maas_yeni)

maas_yeni1 = linear_reg.predict([[11]])     # predict metotu ile de bu hesaplama yapilabilir. x degerline girilecek degeri girmemiz yeterli
print(maas_yeni1)


# visualize line 

array = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]).reshape(-1,1)  #deneyim

plt.scatter(x,y)
plt.show()

y_head = linear_reg.predict(array)  #maas

plt.plot(array, y_head , color = "red")

print(linear_reg.predict([[100]]))




