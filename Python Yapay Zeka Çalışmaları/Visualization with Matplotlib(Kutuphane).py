
# DATAI TEAM



# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 12:22:15 2022

@author: Hasan Emre
"""

#matplotlib kutuphanesi 
#gorsellestirme kutuphanesi
#line plot, scatter plot, bar plot, subplots, histogram

import pandas as pd

df = pd.read_csv("iris.csv") #bir excel dosyasindan bir tablo okuduk

print(df.columns) #sutunlari yazdirdik

print(df.Species.unique) #sadece turleri cagirdik

print(df.info())# tablo hakkinda bilgi aldık

print(df.describe()) #butun bilgilerin tarif ettik ama farkli turleri tek tek yazdirarak karsilastirma yapmak

setosa = df[df.Species == "Iris-setosa"] #tablodan turler bolumunden Iris-setosa adli turu aldık
versicolor = df[df.Species == "Iris-versicolor"] #tablodan turler bolumunden Iris-versicolor adli turu aldık

print(setosa.describe()) #bunlar ile birlikte tek tek ozelliklerini yazdirdik
print(versicolor.describe())

#%% line plot 
import matplotlib.pyplot as plt

df1 = df.drop(["Id"],axis = 1)

#df1.plot()
#plt.show()

setosa = df[df.Species == "Iris-setosa"] #tablodan turler bolumunden Iris-setosa adli turu aldık
versicolor = df[df.Species == "Iris-versicolor"] #tablodan turler bolumunden Iris-versicolor adli turu aldık
virginica = df[df.Species == "Iris-virginica"]

plt.plot(setosa.Id, setosa.PetalLengthCm,color = "red" , label = "setosa") #bir tene tablo icerisine turu degerlere gore cizdik
plt.plot(versicolor.Id, versicolor.PetalLengthCm, color = "green" , label = "versicolor") #color ile renk verdik hangi turun ne oldugunu anlamak icin 
plt.plot(virginica.Id, virginica.PetalLengthCm, color = "blue" , label = "virginica") # label ile renkli cizgilerin adlarini yazdik karisiklik olmasin diye

plt.xlabel("Id") #yan taraflara degerlerin adini yazdik
plt.ylabel("PetalLengthCm")
plt.legend() #label in nerde konumlandirma yapmasi icin kullandik bu sekilde otomatik olarak bir yere koydu
plt.show()# show ile cizelge tablosunu bize gosteriyor

df1.plot(grid = True , alpha = 0.1) #grid yapisi turlere gore degilde sutunlara gore cizelge ciziliyor
plt.show() #sifira gittikce saydamlik artar

#%% scatter plot


setosa = df[df.Species == "Iris-setosa"] #tablodan turler bolumunden Iris-setosa adli turu aldık
versicolor = df[df.Species == "Iris-versicolor"] #tablodan turler bolumunden Iris-versicolor adli turu aldık
virginica = df[df.Species == "Iris-virginica"]

# bu sefer line plot taki gibi cizelge seklinde degilde noktalar seklinde oluyor
plt.scatter(setosa.PetalLengthCm, setosa.PetalWidthCm, color="red" , label="setosa")
plt.scatter(versicolor.PetalLengthCm, versicolor.PetalWidthCm, color="green" , label="versicolor")
plt.scatter(virginica.PetalLengthCm, virginica.PetalWidthCm, color="blue" , label="virginica")
plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm")
plt.legend()
plt.title("Scatter")
plt.show()


#%% histogram 

plt.hist(setosa.PetalLengthCm,bins =30) # bir turde bir özelliğinin kaç tane oldugunu grafigini cikarir
plt.xlabel("PetalLengthCm values")# bins grafiklerin genislik seklini 
plt.ylabel("Freakans")
plt.title("Histogram")
plt.show()

#%% bar plot

import numpy as np


x = np.array([1,2,5,8,6,9,4,7,4,3])# numpy ile bir array olusturduk
y = (x*2+5)

plt.bar(x, y)
plt.title("Bar plot") # bar plot kullanarak bir grafik olusturduk
plt.xlabel("x")
plt.ylabel("y")
plt.show()




x = np.array([1,2,5,8,6,9,4,7,4,3])
a =["Ankara", "Hatay" , "Edirne", "Kırklareli", "İstanbul"]

y = (x*2+5)

plt.bar(a, y)
plt.title("Bar plot")
plt.xlabel("x")
plt.ylabel("y")
plt.show()



#%% subplots

df1.plot(grid = True , alpha = 0.9, subplots = True) #grid yapisi turlere gore degilde sutunlara gore cizelge ciziliyor
plt.show() 


plt.subplot(2,1,1)#2 tane subplotum var 1. column un 1. satiri 
plt.plot(setosa.Id, setosa.PetalLengthCm,color = "red" , label = "setosa") #bir tene tablo icerisine turu degerlere gore cizdik
plt.ylabel("setosa - PetalLengthCm")
plt.subplot(2,1,2)# 2 tane subplotum var 1.column un 2. satiri
plt.plot(versicolor.Id, versicolor.PetalLengthCm, color = "green" , label = "versicolor") #color ile renk verdik hangi turun ne oldugunu anlamak icin 
plt.ylabel("versicolor - PetalLengthCm")
plt.show()


#%% Mustafa Murat Coskun Matplotlib 

import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1,6) # birden altiya kadar sayilari dizi seklinde yazdirdik

y = np.arange(2,11,2)# bunda da iki atlayarak yazdirdik

plt.plot(x, y, "blue")
#plt.show()

plt.subplot(2, 2 , 1)# ikiye iki yazdigimizda dort tane tablo alanı cikiyor 
plt.plot(x, y, "red")

plt.subplot(2, 2 , 2) # dort tane tablo alanini tek tek yazdiriyoruz
plt.plot(y, x, "blue")

plt.subplot(2, 2 , 3)
plt.plot(x,x**3, "green")

plt.subplot(2, 2 , 4)
plt.plot(y**2, y, "black")
plt.show()





#%%



def insertSort(dizi):
    for i in range(1,len(dizi)):
        key = dizi[i]
        j = i-1
        while(j>=0 and key<dizi[j]):
            dizi[j+1] = dizi[j]
            j-=1
            dizi[j+1] = key
dizi = [9,4,7,5,2,8,1,3,6]
insertSort(dizi)
for i in range(len(dizi)):
    print("%d" % dizi[i])



def selectionSort(array, size):
    
    for ind in range(size):
        min_index = ind
 
        for j in range(ind + 1, size):
            # select the minimum element in every iteration
            if array[j] < array[min_index]:
                min_index = j
         # swapping the elements to sort the array
        (array[ind], array[min_index]) = (array[min_index], array[ind])
 
arr = [-2, 45, 0, 11, -9,88,-97,-202,747]
size = len(arr)
selectionSort(arr, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)





















 