# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 06:04:18 2022

@author: Hasan Emre
"""
#%%
var1 = 10
var2 = 20
var3 = var1+var2
print(var3)

var4 = "Hatay"
print(var4)

#%% String

typ = type(var3)
print(typ)

var5 = "Ankara "
var6 = "Hatay"
var7 = var5+var6
print(var7)


var8 = len(var7)
print(var8)

var9 = var6[2]
print(var9)

#%% Numbers

var10 = -50.55487569875515542256
var11 = 37.8

#%% Built in function

str = "1005" #int(str)  

float_num = 15.9 
#int(float_num)
#Out[33]: 15

round(float_num)
#Out[35]: 16

a = 20
b = 50

#sonuc = ((a+b)*100/75)*a/b


def function(a,b):
    
    sonuc = ((a+b)*100/75)*a/b
    
    
    return sonuc

function(a, b)

#%% Default and Flexible

#default

def calculate_circle_circumference(r,pi=3.14): 
    """
    Çemberin çeversini hesaplama
    parametreler(r,pi)
    output = çemberin çevresi
    """
    output = 2*pi*r

    return output
calculate_circle_circumference(2)#Fonksiyonu burada çağırıyoruz


# Flexible


def calculate(height,weight,*args):
    """
    *args bu boy ve kilonun dışında başka birden parametre alabileceği anlamına gelmektedir
    
    """
    print(args)
    output = (weight + height)*args[0]
    return output
calculate(190, 82, 50,56,87,91)

#%% Quiz 1

# int variable yas
# String name isim
# Fonksiyon olacak 
# fonksiyon print(type(),len,float)
# *args soyisim
# default parametresi ile ayakkabı numarası

yas = 10
name = "Emre"
soyisim = "Bağrıyanık "

def function_Quiz(yas, name ,*args , ayakkabı_num = 35):
    print("Çocuğun ismi: ", name , " yaşı: " , yas, " ayakkanı numarası: " , ayakkabı_num)
    print(type(name))
    print(float(yas))
    
    output = args[0]*yas
    return output

function_Quiz(yas, name, soyisim)


#%% lambda fonksiyon

# normal fonksiyon
def calculate(x):
    result = x*x
    return result
print(calculate(3))

#lambda fonksiyon
result2 = lambda x: x*x 
print(result2(2))

#%% liste yapısı
 
List = [1,2,3,4,5,6]
print(type(List))

list_str = ["Hatay" , "Ankara" , "Bursa"]
type(list_str)


value = List[1]
print(value)

last_value = List[-1] # en sondaki degeri alir
print(last_value)

list_divide = List[0:5:2]#0'dan başla 5'e kadar iki iki artarak yaz
print(list_divide)

list_divide = List[0:5]#0'dan başla 5'e kadar yaz
print(list_divide)


List.append(7)# ekleme
print(List)

List.remove(5)#silme
print(List)

List.reverse()#ters çevirme
print(List)

list2 = [1,2,5,8,9,7,4,3,6]
list2.sort()#Sıralama
print(list2)

list2.pop(0)#silme
print(list2)


#%% tuple


t = (1,2,3,3,4,5,6,7)
print(t[3])#indexin karşısındaki sayıyı bulma


print(t.count(3))# bu sayıdan kaç tane olduğunu hesaplıyor

print(t.index(4))#indexin karşısındaki sayıyı bulma


#%% Dictionary


dictionary = {"Emre":19, "Mehmet Ali":20}

print(dictionary)
print(dictionary["Emre"])

print(dictionary.keys())#Anahtarları yani isimleri sadece yazdırıyor
print(dictionary.values())#Değerleri yani sadece sayıları yzadırıyor

def test():
    dictionary = {"Emre":19, "Mehmet Ali":20}
    return dictionary

dic = test()
print(dic.keys())
print(dic["Emre"])
print(dic["Mehmet Ali"])


#%% conditionals(koşullar)
#if elif else statement(ifade)

var1 = 10
var2 = 20

if(var1 > var2):
    print("Var1 var2'den büyüktür")
elif(var1 == var2):
    print("Var1 ve var2 eşittir")
else:
    print("Var1 var2'den küçüktür")



list1 = [1,2,3,4,5,6]
value = 3
if value in list1:
    print("Yes {} value inside the list." .format(value))#değeri listenin içinde
else:
    print("No {} value is not in the list.".format(value)#değeri listenin içinde değil



#%% Quiz


def year_Century(year):
    
    str_year = str(year)
    
    if(len(str_year)<3):
        return 1
    elif(len(str_year)==3):
        if(str_year[1:3] == "00"): #100 200 300 ...
            return int(str_year[0])
        else:
            return int(str_year[0])+1# 109 250...
        
    else:
        if(str_year[2:4] == "00"):#2000 3000
           return int(str_year[:2])
        else:
           return int(str_year[:2])+1 #1750 1860...
            
        
print(year_Century(2003) , "'inci Yüzyıl")

#%% for loops (döngüler)

for i in range(1,11):
    print(i)

for i in "Ankara Hatay":
    print(i)
    
for i in "Ankara Hatay".split():
    print(i)
    
    
list1 = [1,2,58,6,9,4,58,62,31,8,25,78]

print(sum(list1))

count = 0
for x in list1:
    count = count + x
print(count)


#%% while loops

i = 0
while(i<4):
    print(i)
    i += 1
    
print()

list1 = [1,2,58,6,9,4,58,62,31,8,25,78]

i=0
count =0
while(i<len(list1)):
    count += list1[i]
    i+=1
    print(count)

#%% Quiz

# listenin içindeki en küçük sayıyı bulma

list1 = [1,2,3,4,5,6,4,23,67,21,-500,23,451,67]

min = 100000
for i in list1:
    if(i < min):
        min = i
    else:
        continue

print(min)


#%%Class and Constructor (Sınıflar ve yapıcı metotlar)

class Worker:
    raiseRate = 1.8
    counter = 0
    def __init__(self,name ,surname, wage):#constructor
        self.name = name
        self.surname = surname
        self.wage = wage
        self.email = name+surname+"@asd.com"
        
        Worker.counter = Worker.counter + 1 #Çalışan sayısı bulmak için böyle yaptık
        
    def giveNameSurname(self):
        return self.name + " " +self.surname
    
    
    def makeRaise(self):
        self.wage = self.wage + self.wage*self.raiseRate
    
    
worker = Worker("Hasan Emre", "Bağrıyanık", 30000)
worker.makeRaise()
print(worker.name)
print(worker.giveNameSurname())


#class variable
worker1 = Worker("Mehmet Ali", "Sivri", 25000)
print("first wage: ", worker1.wage)
worker1.makeRaise()
print("New wage: ", worker1.wage)
print(Worker.counter)
worker2 = Worker("Veysel", "Uğurlu", 22000)
worker3 = Worker("Ersin", "Tekinel", 15000)

#class example
list1 = [worker,worker1,worker2,worker3]

max_wage = -1
index = -1

for i in list1:
    if(max_wage<i.wage):
        max_wage= i.wage 
        index = i
print(max_wage)

print(index.giveNameSurname())        
        
#%% syntax error

print(9)
#print 9

int(10.0)
int 10.0
#%% exceptions (istisnlar)

k = 10
zero = 0

#if(k == 0 ):
 #   a = 0
  #  print(a)
#else:
 #   a = k/zero
  #  print(a)



try: 
    a = k/zero
    print(a)
except ZeroDivisionError:
    a = 0
    print(a)

#index error
list1 = [1,2,3,4,5]
list1[15]

#module not found error
import numpyy

#file not found error
import pandas as pd
pd.read_csv("asd")


#type error 
"2" + 2 


#value error
int("asd")


try:
    1/0
except: 
    print("except")# Yanlış olduğu zaman except ve finally
    
else:
    print("else")#doğru ise else ve fianlly çalışır
finally: 
    print("done")








