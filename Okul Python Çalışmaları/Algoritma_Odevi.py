# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 12:19:14 2023

@author: Hasan Emre
"""

#kutuphaneler
import time
import random



# Brute Force Algoritmalarını class icine yazildi. Kod karmasikligini onlemek icin bu sekilde kullanilmistir 
class brute_Force():
    
    
    def bruteForceMaxSayiBulma(self, dizi):
        # fonksiyon en buyuk sayiyi buluyor
        max = dizi[0]
        for i in range(1, len(dizi)):
            if dizi[i] > max:
                max = dizi[i]
        return max


    def bruteForceSiralama(self,dizi):
        # Fonksiyon buyukten kucuge dogru diziyi siralar
        for i in range(len(dizi)):
            min = i
            for j in range(i + 1, len(dizi)):
                if dizi[j] < dizi[min]:
                    min = j
        gecici = dizi[i]
        dizi[i] = dizi[min]
        dizi[min] = gecici






class Birinci_Soru():
    
    # class olusturuldu ve icine fonksiyonlar acildi
    def MaxSayiBulma(self):
        
        
        # rastgele 10000 tane sayi uretip diziye atandi
        dizi = [random.randint(0,10000000000) for i in range(10000)]
        
        # zamani hesaplamak icin baslangic ve bitis diyerek o anlık sure yi aliyoruz
        baslangic = time.time()
        print("Quick Sort Algoritması:")
        
        # Siralama fonksiyonunu cagiriyoruz
        Birinci_Soru().Siralama(dizi, 0, len(dizi) -1)
        print("Bulunan Max Sayı: ",dizi[len(dizi) -1])
        
        bitis = time.time()
        print("İşlem boyunca geçen süre: ", bitis - baslangic)
        
        
        # Brute Force Algoritmasi ile max sayi bulmak icin yukaridaki fonksiyonu cagiriyoruz
        başlangic = time.time()
        print("\nBrute Force Algoritması:")
        print("Bulunan Max Sayı: ", brute_Force().bruteForceMaxSayiBulma(dizi))
        
        bitis = time.time()
        print("İşlem boyunca geçen süre: ", bitis - baslangic)
        
        
        # Hizli siralamada quick sort kullanildi
    def quickSort(self,dizi,index1,index2):
        # fonksiyona parametre olarka diziyi aldik 
        # index1 olarak en kucuk sayi olarka aldik
        # index2 olarak en buyuk sayi olarka aldik
        pivot = dizi[index2]
        i = index1-1
        
        for k in range(index1,index2):
            
            if dizi[k] <= pivot:
                i += 1
                
                tmp = dizi[i]
                dizi[k] = dizi[k]
                dizi[k] = tmp
    
    
        temp = dizi[i+1]
        dizi[i+1] = dizi[index2]
        dizi[index2] = temp
    
        return i+1
    
    

    # Olusturdugumuz rastgele olusturdugumuz diziyi burada siraliyoruz
    def Siralama(self,dizi,index1,index2):
        
        if index1 < index2:
            pvtIndex = Birinci_Soru().quickSort(dizi, index1, index2)
             
            Birinci_Soru().Siralama(dizi,index1, pvtIndex -1)
            Birinci_Soru().Siralama(dizi, pvtIndex  +1, index2)
            
            
    
    
    

    
    
    
    
class Dorduncu_Soru():
    
    # class olusturuldu ve icine fonksiyonlar acildi
    def karsilastirma(self):
         # Karsilastirma yapmak icin iki tane rastgele dizi olusturduk
        dizi1 = [random.randint(0,10000000000)for i in range(10000)]
        dizi2 = [random.randint(0,10000000000) for i in range(10000)]

        # Fonksiyonlari cagiriyoruz
        baslangic = time.time()
        print("Quick Sort Sıralaması:")
        
        Dorduncu_Soru().Siralama(dizi1, 0, len(dizi1) -1)
        
        bitis = time.time()
        print("İşlem boyunca geçen süre: ", bitis - baslangic)
        
        
        
        başlangic = time.time()
        print("\nBrute Force Sıralaması:")
        brute_Force().bruteForceSiralama(dizi2)
        
        bitis = time.time()
        print("İşlem boyunca geçen süre: ", bitis - baslangic)
        
        
    # Yukaridaki gibi hizli siralama icin quick sort kullanildi
    def quickSort(self,dizi,index1,index2):
        
        pivot = dizi[index2]
        i = index1-1
        
        for k in range(index1,index2):
            
            if dizi[k] <= pivot:
                i += 1
                
                tmp = dizi[i]
                dizi[k] = dizi[k]
                dizi[k] = tmp
    
    
        temp = dizi[i+1]
        dizi[i+1] = dizi[index2]
        dizi[index2] = temp
    
        return i+1
    
    


    def Siralama(self,dizi,index1,index2):
        
        if index1 < index2:
            pvtIndex = Dorduncu_Soru().quickSort(dizi, index1, index2)
             
            Dorduncu_Soru().Siralama(dizi,index1, pvtIndex -1)
            Dorduncu_Soru().Siralama(dizi, pvtIndex  +1, index2)
            






#  Burada en son olarak classlari icindeki fonksiyonlari ile birlikte cagiriyoruz
        
print("Birinci Sorunun Cevabı: \n")
Birinci_Soru().MaxSayiBulma()

    
print("\n\nDördüncü Sorunun Cevabı: \n")
Dorduncu_Soru().karsilastirma()




