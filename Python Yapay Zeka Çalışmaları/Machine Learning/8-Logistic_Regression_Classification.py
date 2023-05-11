# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 07:58:03 2023

@author: Hasan Emre
"""

#%% library

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#%%

data = pd.read_csv("data_logistic.csv")
data.drop(["Unnamed: 32","id"], axis = 1, inplace= True)  # Siniflandirmada gereksiz olan sutunlari cikardik
data.diagnosis = [1 if i == "M" else 0 for i in data.diagnosis]  # tumor var mi yok sutununda M ve B vardı bunlar object oldugu icin bunlari integer a cevirdik
print(data.info())


y = data.diagnosis.values   # y ye tek bir sutun atıyoruz oda diagnosis
x_data = data.drop(["diagnosis"],axis = 1)  # y ye atadigimiz diognosis i x_data dan cikariyoruz

#%% normalization

# (x - min(x)) / (max(x) - min(x))  normalization formulu butun degerleri 0 ile 1 arasında toplandi.
x = (x_data - np.min(x_data)) / (np.max(x_data) - np.min(x_data)).values

#%% train test split

from sklearn.model_selection import train_test_split
# data nin %80 ini x_train ve y_train olara atadik. geri kalan %20 lik kismi ise x_test ve y_test kismina atadik
# buradaki yuzdelik kismi ayirma test_size ile ayarlaniyor
# data yi her seferinde random olarak bolunur buna bir id vererek sadece bu id uzerinden ayirma yapmasi icin random_state kullanilir 
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state= 42)

# datalarin transpozunu alarak ters ceviriyoruz 
x_train = x_train.T 
x_test = x_test.T
y_train = y_train.T
y_test = y_test.T



#%%  parameter initialize and sigmoid function
# dimension = 30  dimension => feature (nitelikler) anlamına gelir bizim datamizda 30 tane featuremuz var 

def initialize_weights_and_bias(dimension):
    
    w = np.full((dimension,1),0.01)  # weights deki butun featurelara (30) 0.01 degerini atiyoruz
    b = 0.0
    return w,b

# w,b = initialize_weights_and_bias(30)

def sigmoid(z):
    
    y_head = 1 / (1+ np.exp(-z))
    return y_head
# sigmoid(0)

#%%   

def forward_backward_propagation(w,b,x_train,y_train):
    # forward propagation
    z = np.dot(w.T, x_train) + b
    y_head = sigmoid(z)
    loss = -y_train*np.log(y_head) - (1-y_train)*np.log(1-y_head)
    cost = (np.sum(loss))/x_train.shape[1]    
    
    #backward propagation
    derivative_weight = (np.dot(x_train,((y_head-y_train).T)))/x_train.shape[1]
    derivative_bias = np.sum(y_head-y_train)/x_train.shape[1]
    gradients = {"derivative_weight": derivative_weight, "derivative_bias": derivative_bias}
    
    return cost,gradients



#%% Updating (learning) parameters

def update(w, b, x_train, y_train, learning_rate, number_of_iteration):
    cost_list = []
    cost_list2 = []
    index = []
    
    # Updating (learning) parameters isnumber_of_iteration times
    for i in range(number_of_iteration):
        cost,gradients = forward_backward_propagation(w, b, x_train, y_train)
        cost_list.append(cost)
        
        # lets update
        w = w - learning_rate * gradients["derivative_weight"]
        b = b - learning_rate * gradients["derivative_bias"]
        # if i % 10 == 0:
        #     cost_list2.append(cost)
        #     index.append(i)
        #     print("Cost after iteration %i: %f"  %(i,cost))
            
    #we update (learn) parameters weights and bias
    parameters = {"weight": w, "bias": b}
    # plt.plot(index,cost_list2)
    # plt.xticks(index, rotation = "vertical")
    # plt.xlabel("Number Of Iteration")
    # plt.ylabel("Cost")
    # plt.show()
    return parameters, gradients, cost_list


#%% prediction 

def predict(w, b, x_test):
    # x_test is a input for forward propagation
    z = sigmoid(np.dot(w.T, x_test) + b)
    y_prediction = np.zeros((1, x_test.shape[1]))
    #if z is bigger than 0.5, our prediction is sign one (y_head = 1)
    #if z is smaller than 0.5, our prediction is sign zero (y_head = 0)
    
    for i in range(z.shape[1]):
        if z[0,i] <= 0.5:
            y_prediction[0,i] = 0
        else:
            y_prediction[0,i] = 1
    
    return y_prediction
        

#%%   logistic regression 
def logistic_regression(x_train, y_train, x_test, y_test, learning_rate, num_iteration):
    #initialize
    dimension = x_train.shape[0]  # that is 30
    w, b = initialize_weights_and_bias(dimension)
    # do not change learning rate
    
    parameters, gradients, cost_list = update(w, b, x_train, y_train, learning_rate, num_iteration)
    
    y_prediction_test = predict(parameters["weight"], parameters["bias"], x_test)
    
    #print test errors
    print("Test Accuracy: {} " .format(100 - np.mean(np.abs(y_prediction_test - y_test)) * 100))
    
for i in np.arange(-1,1,0.01):
    learning_rate = i
    print("learning rate: ", i)
    logistic_regression(x_train, y_train, x_test, y_test, learning_rate = learning_rate,  num_iteration = 200)    
     
    # en fazla learning_rate 1 iken bum_iteration = 210 değerinde sabit bir sekilde kaliyor
    # en fazla learning_rate 3 iken bum_iteration = 70 değerinde sabit bir sekilde kaliyor



#%%  sklearn with LR
# yukarıda yapilan elle hesaplamaya göre daha iyi sonuc buluyoruz. Cunku kutuphanede daha cok parametre var
# trainlere bakiyoruz ona gore ters cevirme islemi yapıyoruz yani transpozunu alıyoruz
from sklearn.linear_model import LogisticRegression

lr = LogisticRegression(random_state=42, max_iter=150)
lr.fit(x_train.T, y_train.T)
print("Test accuracy {}". format(lr.score(x_test.T, y_test.T)))












