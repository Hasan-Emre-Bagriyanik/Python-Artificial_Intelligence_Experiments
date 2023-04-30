# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 05:48:39 2023

@author: Hasan Emre
"""

# import library
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# import dataset
data = pd.read_csv("KNN_data.csv")
data.head()

data.drop(["id", "Unnamed: 32"],axis = 1, inplace= True)
data.tail()
# maligant = M   kotu huylu tumor
# benign = B     iyi huylu tumor

#%%

#dataset visiulaize
M = data[data.diagnosis == "M"]
B = data[data.diagnosis == "B"]

# scatter plot
plt.scatter(M.radius_mean, M.texture_mean, color = "red", label = "kotu" ,alpha=0.3)
plt.scatter(B.radius_mean, B.texture_mean, color = "green", label = "iyi", alpha= 0.3)      
plt.legend()
plt.xlabel("radius_mean")
plt.ylabel("texture_mean")
plt.show()

#%%

data.diagnosis = [1 if i == "M" else 0  for i in data.diagnosis]
y = data.diagnosis.values
x_data = data.drop(["diagnosis"], axis= 1)
  

#normalization
x = (x_data - np.min(x_data)) / (np.max(x_data) - np.min(x_data))



#%% train test split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.3, random_state=1)

#%% knn model
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors= 3) # n_neighbors = K
knn.fit(x_train, y_train)
prediction = knn.predict(x_test)

print(" {} nn score: {} ".format(3, knn.score(x_test, y_test)))

#%% find k value

score_list = []

for i in range(1,15):
    knn2 = KNeighborsClassifier(n_neighbors= i)
    knn2.fit(x_train, y_train)
    score_list.append(knn2.score(x_test, y_test))
    
plt.plot(range(1,15), score_list)
plt.xlabel(" k values")
plt.ylabel("Accuracy")
plt.show()



















