# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 06:53:41 2023

@author: Hasan Emre
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%% create database

#class 1
x1 = np.random.normal(25,5,1000)  #25 ortalamaya sahip 1000 tane deger uret. %66 si 25-5 ile 25+5 arasinda olacaktir.
y1 = np.random.normal(25,5,1000)
# class 2
x2 = np.random.normal(55,5,1000)  
y2 = np.random.normal(60,5,1000)
# class 3
x3 = np.random.normal(55,5,1000)  
y3 = np.random.normal(15,5,1000)

x = np.concatenate((x1,x2,x3), axis = 0)
y = np.concatenate((y1,y2,y3), axis = 0)

dictionary = {"x":x, "y":y}

data = pd.DataFrame(dictionary)


plt.scatter(x1,y1)
plt.scatter(x2,y2)
plt.scatter(x3,y3)
plt.show()

#%% kmeans algoritmasi bunu gorecek

# plt.scatter(x1,y1, color = "black")
# plt.scatter(x2,y2, color = "black")
# plt.scatter(x3,y3, color = "black")
# plt.show()

#%% KMEANS

from sklearn.cluster import KMeans

wcss = []

for k in range(1,15):
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(data)
    wcss.append(kmeans.inertia_)  # 1'den 15'e kadar k degerleri urettik ve bunlara gore wcss degerlerini bulacagiz.
                                  # bu degerleri grafikte cizdirecegiz ve dirsek seklinde kirilma oldugu yeri k degeri olarka alacagiz.
plt.plot(range(1,15), wcss)
plt.xlabel("number of k (cluster) value")
plt.ylabel("wcss")
plt.show()

# k degerini 3 olarak alacagiz cunku dirsek seklinde kirilma bu noktada olmaktadir.

#%% k = 3 icin modelim

kmeans2 = KMeans(n_clusters=3)
clusters = kmeans2.fit_predict(data)

data["label"] = clusters

plt.scatter(data.x[data.label == 0],data.y[data.label == 0],color = "red")
plt.scatter(data.x[data.label == 1],data.y[data.label == 1],color = "green")
plt.scatter(data.x[data.label == 2],data.y[data.label == 2],color = "blue")
plt.scatter(kmeans2.cluster_centers_[:,0],kmeans2.cluster_centers_[:,1],color = "black") # cluster ile orta noktalari gosterdik
plt.show()
# kmeans datamizi dogru tahmin etti.
        








 











