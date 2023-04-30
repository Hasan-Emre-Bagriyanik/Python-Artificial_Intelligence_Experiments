# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 08:41:09 2023

@author: Hasan Emre
"""

# import library
import numpy as np
import pandas as pd


# import dataset
data = pd.read_csv("KNN_data.csv")
data.head()

data.drop(["id", "Unnamed: 32"],axis = 1, inplace= True)
data.tail()
# maligant = M   kotu huylu tumor
# benign = B     iyi huylu tumor

#%%

data.diagnosis = [1 if i == "M" else 0  for i in data.diagnosis]
y = data.diagnosis.values
x_data = data.drop(["diagnosis"], axis= 1)
  

#normalization
x = (x_data - np.min(x_data)) / (np.max(x_data) - np.min(x_data))

 #%% train test split
 
from sklearn.model_selection import train_test_split
 
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.25, random_state=42)

#%% 
from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier()
dt.fit(x_train, y_train)

print("score: ", dt.score(x_test, y_test))

