# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 05:28:47 2022

@author: Hasan Emre
"""

#numpy kütüphanesi kullanımı

import numpy as np

#numpy basics

array = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])#3*15 vector

print(array.shape)

a = array.reshape(3,5)#yukarıdaki dizinin kaça kaç bir matris olacağını burada ayarlanır
print("Shape: ",a.shape)# kaça kaç bir matris olduğunu gösteriyor
print("dimension: ", a.ndim)# kaç boyutlu olduğunu 

print("data type: ", a.dtype.name)#türünü öğrenmek için 
print("size: ",a.size)# boyutunu öğrenmek için

print("type: ",type(a))#tipini öğrenmke için 

array1 = np.array([[1,2,3,4],[5,6,7,8],[9,8,7,5]])#Bu 3*4 bir matristir.Ayrı ayrı yazdığımız için yukarıdaki gibi reshape ile tekrardan bölmeye gerek kalmadı

print(np.arange(1,100,3)) #1'den baslayip 100'e kadar ucer ucer artarak dizi olusturur

zeros1 = np.zeros(10) #sifirlardan olusan tek boyutu dizi olusur
zeros = np.zeros((3,4)) #demetler seklinde olusturursam Sıfırlardan oluşan bir matris oluşturur
zeros[0,0] = 5  #Sıfırlarla oluşan bir matrisi kendimiz tek tek değer atayabiliriz
print(zeros)

print(np.ones((3,4))) #birlerden oluşan bir 3*4 matris oluşturduk 

np.empty((2,4)) # boş bir array oluşturuyor

a = np.arange(10,50,5)# 10'dan başlayarak 50'ye kadar beş beş artarak dizi oluşturur
print(a)

b = np.arange(1,20,1.5)
print(b)

print(np.eye(5)) #♣ birim matris olusur


print(np.random.randint(5,20,size=(5,4))) #5'ten baslayarak 20'ye kadar 5 satirlik 4 sutunluk bir rastgele integer sayilar ile matris olusur
print(np.random.rand(5,20,5)) #5'ten baslayarak 20'ye kadar 5 satirlik 4 sutunluk bir rastgele float sayilar ile matris olusur
print(np.random.randn(5)) #arti eksi  degerler alir 
a = np.linspace(10,50,20) # 10'dan 50'ye kadar 20 tane rastgele sayı yazarak dizi oluşturuyor
print(a)


#%% numpy basic operations

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a+b)#iki matrisi toplama 
print(a-b)#İki matrisi çıkarma 
print(a**2)#iki matrisin karesini alma


print(a<2)#a matrisinin bir değerden küçük olup olmadığı koşulunun kontrol etme


a = np.array([[1,2,3],[4,5,6]])
b = np.array([[1,2,3],[4,5,6]])


print(a*b) #Matrisi karşılıklı çarpma


a.dot(b.T) #Matris çarpımı a matrisi(2,3), b matrisi(2,3) olduğu için hata aldık ama b nin transpozunu alırsak (2,3) (3,2) olur ve çarpım gerçekleşir

print(np.exp(a))

a = np.random.random((5,5)) # 5*5 random sayılar ile matris oluşturma

print(a.sum())# matrislerin içinin tümünün toplamı 
print(a.max())# en büyük sayı 
print(a.min())# en küçüks sayı
print(a.argmax())# maximum sayinin kacinci indexde oldugunu gösterir

print(a.sum(axis=0)) # Sutünları toplar 
print(a.sum(axis=1)) # satırları toplar

print(np.sqrt(a)) #matrisin tek tek karaköklerini alır
print(np.square) # matrisin karesini alıyor

print(np.add(a,a)) # a ile a matrisini topluyor

print(np.linalg.det(a)) # a matrisinin determinatını bulur
print(round(np.linalg.det(a))) # daha duzgun gorunmesini saglar


#%% indexing and slicing

array = np.array([1,2,3,4,5,6,7])# vector dimenstion = 1 tek satırlık matris

print(array[0])

print(array[0:4])# ssıfırncı indexten 3'üncü indexe kadar matrisi yazdırır

reverse_array = array[::-1] # dizi ters çevirme
print(reverse_array)

print()

array1 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(array1)


print(array1[1,1])# ilk sayı satırı temsil ediyor ikinci sayı ise sutünu temsil ediyor

print(array1[:,1])#satır içerisinden birinci indexli sutünu al

print(array1[1,1:4])#1. indexli satırdan 1'den 4'e kadar olan sayıları al

print(array1[-1,:])#son satırı al
print(array1[:,-1])#son sutünu al 


#%% shape manipulation 

array = np.array([[1,2,3],[2,3,4],[7,8,9]])

a = array.ravel() # çoklu bir matrisi tek satır haline getirir
print(a)

array2 = a.reshape(3,3) # reshape ile matris boyutu değiştiryoruz ama farklı bir matris oluşturarak atıyoruz
print(array2)

arrayT = array2.T # matrisin transpozu alınıyor
print(arrayT)

print(arrayT.shape) # matrisin kaça kaç olduğunu gösterir

array3 = np.array([[1,2],[3,4],[5,6]])
print(array3)
print(array3.reshape(2,3))#reshape anlık olarak o dizi değiştiriyor ama kalıcı olarak değil
print(array3)
array3.resize((1,6))#resize kalıcı olarak matrisin boyutunu değiştirir
print(array3)

#%% stacking arrays matrisleri birleştirme 

array1 = np.array([[1,2],[3,4]])
array2 = np.array([[-1,-2],[-3,-4]])


#veritical: iki matrisi dikey bir şekilde birleştirir
array3 = np.vstack((array1,array2))
print(array3)

#horizontal: iki matrisi yatay bir şekilde birleştirir
array4 = np.hstack((array1,array2))
print(array4)

#%% convert and copy

liste = [1,2,3,4,5]

array = np.array(liste) # listeyi dizinin içine atıyoruz
print(array)


a = np.array([1,2,3])

b = a  # burada hepsi birlikte değişti
b[0] = 5
c = a
print(a)
print(b)
print(c)


d = np.array([1,2,3,4])

e = d.copy() #burada hepsi birlikte değişmedi copy yazdığımız için
e[0] = 5
f = d.copy()

print(d)
print(e)
print(f)
















