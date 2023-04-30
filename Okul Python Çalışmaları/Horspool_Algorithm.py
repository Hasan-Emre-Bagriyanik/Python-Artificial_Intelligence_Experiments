# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 15:56:46 2023

@author: Hasan Emre
"""

def horspool_algorithm(metin, aranacak_kelime):
    # metnin ve aranacak kelimenin uzunluklarini aliyoruz.
    n = len(metin)
    m = len(aranacak_kelime)
    
    if m > n:
        return 0
    shift = {}
    
    # Arama yaparken kelime kelime degilde harf harf arama yaptigi icin bize kelime sayisini vermesi icin sayac koyuldu.
    # Bu sayac bize kelimenin kac kere dondugunu gosterecek 
    for i in range(m - 1):
        shift[aranacak_kelime[i]] = m - i - 1
        
    sayac = 0
    i = m - 1
    
    while i < n:
        k = 0
        
        while k < m and aranacak_kelime[m - 1 - k] == metin[i - k]:
            k += 1
            
        if k == m:
            sayac += 1
            
        if metin[i] in shift:
            i += shift[metin[i]]
            
        else:
            i += m
            
    return sayac


# Metin dosyasini yolunu belirterek txt dosyasini okuyoruz 
metin = "alice_in_wonderland.txt"
with open(metin, "r") as file:
    metin = file.read()
    
    
# Sabit verilen kelimeleri direk kac defa gectigini hesaplayıp yazdırıyoruz
aranacak_kelime = "upon"
sayac = horspool_algorithm(metin, aranacak_kelime)
print("\n'{0}' kelimesi metin dosyasında {1} kez geçiyor.".format(aranacak_kelime, sayac))

aranacak_kelime = "sigh"
sayac = horspool_algorithm(metin, aranacak_kelime)
print("\n'{0}' kelimesi metin dosyasında {1} kez geçiyor.".format(aranacak_kelime, sayac))

aranacak_kelime = "Dormouse"
sayac = horspool_algorithm(metin, aranacak_kelime)
print("\n'{0}' kelimesi metin dosyasında {1} kez geçiyor.".format(aranacak_kelime, sayac))

aranacak_kelime = "jury-box"
sayac = horspool_algorithm(metin, aranacak_kelime)
print("\n'{0}' kelimesi metin dosyasında {1} kez geçiyor.".format(aranacak_kelime, sayac))

aranacak_kelime = "swim"
sayac = horspool_algorithm(metin, aranacak_kelime)
print("\n'{0}' kelimesi metin dosyasında {1} kez geçiyor.".format(aranacak_kelime, sayac))
    

# Kullanici sabit kelimeler disinda da bir kelime aratmak istersediye kullanicidan da kelime alip kac defa dondugunu gosteriyoruz
aranacak_kelime = input("\n\nAramak istediğiniz kelimeyi giriniz: ")
sayac = horspool_algorithm(metin, aranacak_kelime)

print("'{0}' kelimesi metin dosyasında {1} kez geçiyor.".format(aranacak_kelime, sayac))

