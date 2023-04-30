# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 15:53:19 2023

@author: Hasan Emre
"""

from sklearn.datasets import load_iris
import pandas as pd


#%%

iris = load_iris()

data = iris.data
feature_names = iris.feature_names
y= iris.target

df = pd.DataFrame(data, columns = feature_names)
df["sinif"] = y

x = data
#%% PCA

from sklearn.decomposition import PCA
# burada 4 boyutlu dataframe i 2 b boyutluya cevirdik
pca = PCA(n_components=2, whiten=True) # Whiten  = normalize
pca.fit(x)

# yukarida matematik bolumunu yaptık ama donusturmedik simdi transform ile donusturme islemi yapıyoruz
x_pca = pca.transform(x) 

print("Variance ratio: ", pca.explained_variance_ratio_)
# Variance ratio:  [0.92461872 0.05306648]
# 0.92461872 ilk kisim principle component p1
# 0.05306648 ikinci kisim ise second component p2


print("Sum : ", sum(pca.explained_variance_ratio_))
# Sum :  0.977685206318795
# datanin %97 lik kismina sahipiz %3 luk kismi kayip
#%%  2D

df["p1"] = x_pca[:,0]
df["p2"] = x_pca[:,1]

color = ["red","green","blue"]

import matplotlib.pyplot as plt

for i in range(3):
    plt.scatter(df.p1[df.sinif == i], df.p2[df.sinif == i], color = color[i], label = iris.target_names[i])

plt.legend()
plt.xlabel("p1")
plt.ylabel("p2")

plt.show()

