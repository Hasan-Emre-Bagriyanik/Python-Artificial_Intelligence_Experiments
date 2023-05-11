
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 07:43:42 2023

@author: Hasan Emre
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%% create database

#class 1
x1 = np.random.normal(25,5,100)  #25 ortalamaya sahip 1000 tane deger uret. %66 si 25-5 ile 25+5 arasinda olacaktir.
y1 = np.random.normal(25,5,100)
# class 2
x2 = np.random.normal(55,5,100)  
y2 = np.random.normal(60,5,100)
# class 3
x3 = np.random.normal(55,5,100)  
y3 = np.random.normal(15,5,100)

x = np.concatenate((x1,x2,x3), axis = 0)
y = np.concatenate((y1,y2,y3), axis = 0)

dictionary = {"x":x, "y":y}

data = pd.DataFrame(dictionary)


plt.scatter(x1,y1)
plt.scatter(x2,y2)
plt.scatter(x3,y3)
plt.show()

#%% dendrogram

from scipy.cluster.hierarchy import linkage, dendrogram

merg = linkage(data, method="ward")
dendrogram(merg, leaf_rotation=90)
plt.xlabel("data points")
plt.ylabel("euclidean dsitance")
plt.show()
# dendrogram ile grafigimizi cizdirdik ve kesismeyen en uzun yerden düz bir cizgi cizdigimizde 3 yerden kesmektedir yani 3 tane clusterimiz olacaktir.

#%%  Hierarcical Clustering

from sklearn.cluster import AgglomerativeClustering
hierarcical_cluster = AgglomerativeClustering(n_clusters=3, affinity="euclidean", linkage="ward")
cluster = hierarcical_cluster.fit_predict(data)

data["label"] = cluster

plt.scatter(data.x[data.label == 0],data.y[data.label == 0],color = "red")
plt.scatter(data.x[data.label == 1],data.y[data.label == 1],color = "green")
plt.scatter(data.x[data.label == 2],data.y[data.label == 2],color = "blue")
plt.show()



