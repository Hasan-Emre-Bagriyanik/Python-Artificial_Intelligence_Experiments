# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 08:48:07 2023

@author: Hasan Emre
"""

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
 
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.15, random_state=42)

#%%  decision tree

from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier()
dt.fit(x_train, y_train)

print("decision tree score: ", dt.score(x_test, y_test))


#%% random forest

from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(n_estimators= 100, random_state=1)
rf.fit(x_train, y_train)
print("Random forest algo result: ",rf.score(x_test, y_test))


y_pred = rf.predict(x_test)
y_true = y_test

#%% confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_true, y_pred)

#%% cm visualization

import seaborn as sns
import matplotlib.pyplot as plt

f, ax = plt.subplots(figsize = (5,5))
sns.heatmap(cm, annot = True ,linewidths=0.5, fmt = ".0f", ax=ax)
plt.xlabel("y_pred")
plt.ylabel("y_true")
plt.show()



