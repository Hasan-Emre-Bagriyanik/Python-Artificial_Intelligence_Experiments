
# Mustafa Murat Coskun Ornekleri

import pandas as pd
import numpy as np
from numpy.random import randn

pd.Series([10,20,30,40],["Emre","Hasan","Sametcan","İbrahim"])#series ile iki şeyi yan yana yazabilirsin fazladan baska seyler yazmak istersek ise dictionary kullanabiliriz

#3'e  bir matris rastgele oluturuluyor sol tarafına a b c diye index veriliyor üst tarafına ise columnlar veriliyor
df = pd.DataFrame(data=randn(3,3),index= ["A", "B","C"] ,columns=["columns1","columns2","columns3"] )
print(df)

print(df.loc["A"]) # A'ninci satiri yazdiriyor
print(df.loc["A","columns1"])# A'ninci satiri ve columns1 i yazdiriyor
print(df.loc[:,["columns1","columns3"]]) # Tum satirlari ve sadece columns1 ve columns3 aliyor


df1 = pd.DataFrame(randn(4,3),["A", "B","C", "D"], ["columns1","columns2","columns3"])
print(df1) #4' 3'luk bir tablo olusturduk 

print(df1 > 0) # buyuklugune gore true false dondure islemi yapacak

print(df1[df1 > 0]) # true donen yerleri yazdiracak ama false donen yerleri ise nan donecek
print(df1["columns1"] > 1) # sadece bir columns a gore true false donderir
print(df1[df1["columns1"] > 0]) # Aldigimiz tek sutunda kosulu true donen satırı komple aliyor
print(df1[(df1["columns1"] > -1)  & ( df1["columns2"] > 0)]) #iki kosuluda saglayan satirlar komple geliyor
print(df1[(df1["columns1"] > -1)  | ( df1["columns2"] > 0)]) #iki kosuluda saglayan satirlar komple geliyor

# Yeni bir sutun eklemek icin 
df1["columns4"] = pd.Series(randn(4),["A","B","C","D"])
#♣ bu sekilde daha kisa bir sekilde yapilabilir
df1["columns5"] = randn(4)
# baska bir sutun ekledik
df1["columns6"] = ["values1","values2","values3","values4"]

# Sutunlari a b c d olan yere columns6'yi atadik ve inplace ile kalici bir sekilde duzenledik
df1.set_index("columns6", inplace=True)
print(df1.index.names) # indexlerin adlarini gosterir kac tane varsa

# multiIndex
# dis gruplar
outerIndex = ["Group1" , "Group1", "Group1","Group2" , "Group2", "Group2","Group3" , "Group3", "Group3" ]
# ic gruplar
innerIndex = ["Index1","Index2","Index3","Index1","Index2","Index3","Index1","Index2","Index3"]
hierarchy = list(zip(outerIndex,innerIndex)) # iki grubu birbirlerine liste seklinde birlestirdik
hierarchy = pd.MultiIndex.from_tuples(hierarchy)# listeyi coklu indexe atadik
df = pd.DataFrame(randn(9,3),hierarchy,columns=["Column1","Column2","Column3"])# ve burada bir tablo olusturduk

df["Column1"] #birinci sutunda olanlar geldi
df.loc["Group1"] # sadece grup1 deki sayilar geldi
df.loc["Group1"].loc["Index1"]["Column1"] # birinci gruptaki Index birden sutun1'deki degeri yazdirdik

df.index.names = ["Groups","Indexes"] # olusturdugumuz multiIndexlere isimler koyduk
df.xs("Group1").xs("Index1").xs("Column1") # xs() ile indexlerin icindeki sayilari bulmamiza yariyor
df.xs("Index1", level=("Indexes")) # bu sekilde yaptigimizda grupların sadece birinci indexleri gelmektedir

#%% kayip ve bozuk veriler


arr = np.array([[10,5,np.nan],[15,np.nan,np.nan],[8,np.nan,7]]) # bozuk verili bir matris girdik 
df = pd.DataFrame(arr,index=["index1","index2","index3"], columns=["column1","column2","column3"]) # bu matrisi düzenledik

df.dropna() # burada bozuk veri olan yani "nan" olan verileri bulunan satirlari siliyor komple
print(df.dropna(axis=1)) # bozuk veri olan sutunlari siliyor

df.dropna(thresh=2) # burada thresh ile satirda iki sağlam veri varsa o satirlari yazdir

df.fillna(value=1) # bu etiket ile "nan" olan degerlerin hepsini icindeki degeri atar

df.sum().sum() # matrisdeki tüm sayilari toplar (nan'lar haric)

df.size # matrisin icinde kac tane deger oldugunu soyler(nan'lar da icinde)

df.isnull().sum().sum() # nan olan degerlerden kac tane oldugunu soyler

#matrisin icindeki sayilari toplayarak toplanan sayiya bolerek ortalamasini bulup "nan" olan yerler yazdirdik
def calculateMean(df):
    totalSum = df.sum().sum()
    totalNum = df.size - df.isnull().sum().sum()
    return totalSum / totalNum 

df.fillna(value=calculateMean(df))
 


#%% GroupBy operasyonu 



dataset = {
        "Departman":["Bilişim","İnsan Kaynakları","Üretim","Üretim","Bilişim","İnsan Kaynakları"],
        "Çalışan": ["Mustafa","Jale","Kadir","Zeynep","Murat","Ahmet"],
        "Maaş":[3000,3500,2500,4500,4000,2000]
        }

df = pd.DataFrame(dataset) # bir tene atblo olusturduk 

DepGroup = df.groupby("Departman") # groupBy ile gruplama yaptik 

DepGroup.sum() # aynı departmanda bulunanları tek cati altinda topluyor

int(DepGroup.sum().loc["Bilişim"]) # departmanlardan birinin maasini yazdiriyor

DepGroup.count() # hangi gruptan kac tane var onun sayisini soyluyor

DepGroup.max() # ayrı ayrı departman bolumlerinde maas ve calisanlarin arasından en buyukleri seciliyor

DepGroup.min() # en dusuk değerler

DepGroup.min()["Maaş"]["Bilişim"] #tablodaki bilisim departmanindan en dusuk maasi veriyor

DepGroup.mean() # maaslarin ortalamsini soyluyor

DepGroup.mean()["Maaş"]["İnsan Kaynakları"] # konum vererek istedigimiz yerin ortalamsini alabiliriz



#%%  Merge, Join and Concatenate (birlestirme)

#concat
dataset1 = {
    "A": ["A1","A2","A3","A4"],
    "B":["B1","B2","B3","B4"],
    "C":["C1","C2","C3","C4"],
}
    
dataset2 = {
    "A": ["A5","A6","A7","A8"],
    "B":["B5","B6","B7","B8"],
    "C":["C5","C6","C7","C8"],
}

df1 = pd.DataFrame(dataset1,index=[1,2,3,4])# iki farklı data frame olusturduk
df2 = pd.DataFrame(dataset2,index=[5,6,7,8])


pd.concat([df1,df2]) # iki dataframe i alt alta birlestirdik

pd.concat([df1,df2],axis=1) # iki dataframe i yan yana birlestirdik 

# join index degerine gore siralama yapar

dataset1 = {
    "A" : ["A1","A2","A3","A4"],
    "B" : ["B1","B2","B3","A4"],
}
dataset2 = {
    "X" : ["X1","X2","X3"],
    "Y" : ["Y1","Y2","Y3"],
    
}
df1 = pd.DataFrame(dataset1,index = [1,2,3,4])  #iki farklı dataframe olusturduk
df2 = pd.DataFrame(dataset2,index = [1,2,3])


df1.join(df2) #df1'e df2'yi join ettik yani ekledik. sonuc ilk bastakine gore sekillleniyor. left join olarak olusur

df2.join(df1)# tam tersi

#merge column degerine gore siralama yapar
dataset1 = {
    "A" : ["A1","A2","A3"],
    "B" : ["B1","B2","B3"],
    "anahtar" : ["K1","K2","K3"]
}

dataset2 = {
    "X" : ["X1","X2","X3","X4"],
    "Y" : ["Y1","Y2","Y3","Y4"],
    "anahtar" : ["K1","K2","K5","K4"]
}

df1 = pd.DataFrame(dataset1,index = [1,2,3]) 
df2 = pd.DataFrame(dataset2,index = [1,2,3,4])

pd.merge(df1, df2, on="anahtar") #bu inner join gibi iki tarafta da aynı olan "anahtar" columna gore siralama yaptik


#%% DataFrame Operasyonlari

df = pd.DataFrame({
    "Column1":[1,2,3,4,5,6],
    "Column2":[100,100,200,300,300,100],
    "Column3":["Mustafa","Kamil","Emre","Ayşe","Murat","Zeynep"]
})


df.head(n=3) # tablonun ilk 3 satirini alir

df["Column2"].unique() # tekil olan degerleri sirasiyla yaziyor

df["Column2"].nunique()# benzersiz kaç tane oldugunu sayı olarak yaziyor

df["Column2"].value_counts() # her bir elemanin o degerde kac tane oldugunu soyluyor

df[(df["Column1"] >= 4)& (df["Column2"] == 300)]

# bir fonksiyon ile column2 deki degerli apply fonksiyonu ile tek tek uyguladik
def times3(x):
    return x*3

df["Column2"] = df["Column2"].apply(times3)

df["Column2"].apply(lambda x : x*2) # yukaridaki islevi goren farkli metot

df["Column3"].apply(len) # stringlerin uzunluklarina gore boyutlandirdi

df.drop("Column3",axis=1, inplace=True) # column3 u sildik

df.columns # kac tane sutun varsa tek tek adlarini yazdirir

df.index # index degerinde ise baslangic degerinden son degere kadar  kac kac artigini gosterir

len(df.index) # bu da direk olarak kac tane sutun oldugunu gosterir

df.sort_values("Column2" ) # bu kucukten buyuge dogru siraliyor

df.sort_values("Column2", ascending = False)  #buda buyukten kucuge dogru siraliyor

# pivot tale olusturma 

df = pd.DataFrame({
    "Ay" : ["Mart","Nisan","Mayıs","Mart","Nisan","Mayıs","Mart","Nisan","Mayıs"],
    "Şehir":["Ankara","Ankara","Ankara","İstanbul","İstanbul","İstanbul","İzmir","İzmir","İzmir"],
    "Nem":[10,25,50,21,67,80,30,70,75]
})

df.pivot_table(index="Ay", columns="Şehir", values = "Nem")  # tabloyu daha duzenli kullanmak icin yapilabilir


#%% DataSet Okuma yontemleri

dataset = pd.read_csv("USvideos.csv")# baska bir dosyayi okumak icin kullanilir

dataset1 =  dataset.drop(["video_id","trending_date"] ,axis = 1) # sutun silme islemi yaptık

dataset1.to_csv("NewUSvideos.csv") # yeni olusan tabloyu dosya haline getirdik


#%%   QUIZ

## Pandas Veri Analizi - U.S Major League Soccer Salaries Veri Analizi

##### Pandas'ı Dahil Edin
import pandas as pd

##### VeriSetini Okuyun

soccer = pd.read_csv("mls-salaries-2017.csv")
print(soccer)

##### ilk 10 Veriyi Okuyun
soccer.head(n = 10)

##### Kac tane Veri Oldugunu Bulun(Satir Sayisi)
len(soccer.index)

##### Tum Maaslarin Ortalamasi Bulun.
soccer["base_salary"].mean()

##### En yuksek maasi bulun
soccer["base_salary"].max()

##### En yuksek tazminata sahip futbolcunun soyadini bulun
soccer[soccer["guaranteed_compensation"].max() == soccer["guaranteed_compensation"]]["last_name"]

##### "Gonzalez Pirez" isimli futbolcunun oynadigi mevkiyi bulun.
soccer[soccer["last_name"] == "Gonzalez Pirez"]["position"].iloc[0]

##### Mevkilere gore futbolculari gruplayarak mevkilerde ortalama maaslari bulun
soccer.groupby("position").mean()

##### Verisetinde kac farkli mevki oldugunu hesaplayin.
soccer["position"].nunique()

##### Her mevkide kac oyuncunun oldugunu hesaplayin
soccer["position"].value_counts()

##### Her takimda kac kisinin oynadigini hesaplayin.
soccer["club"].value_counts()

# oyuncularin isminde "son" icerenleri yazdir

def re_find(last_name):
    if "son" in last_name.lower():
        return True
    return False
soccer[soccer["last_name"].apply(re_find)]




#%% QUIZ 2

# youtube analizi

##### Pandas'ı Dahil Edin
import pandas as pd

##### Youtube Dataset'ini Okuyun
youtube =  pd.read_csv("USvideos.csv")

##### İlk 5 Veriyi gösterin
youtube.head(n = 5)

##### Dataseti aşağıdaki sütünları silerek güncelleyin.
thumbnail_link,video_id,trending_date,publish_time,thumbnail_link,comments_disabled,ratings_disabled,video_error_or_removed
youtube.drop(["thumbnail_link","publish_time","thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed"],axis = 1 ,inplace=True)

##### Kaç tane Sütün ve Kaç Tane Satır Olduğunu Bulun.
len(youtube.columns)
len(youtube.index)

##### Beğeni ve Beğenmeme sayılarının ortalamasını bulun
youtube["likes"].mean()







#%% DATAI TEAM 



# 1) pandas hizli ve etkili for dataframes
# 2) csv ve text dosyalarÄ±na acip inceleyip sonuclarimiza bu dosya tiplerine rahat bir sekilde kaydedbilir.
# 3) pandas bizim isimizi kolaylastiriyor for missing data
# 4) reshape yapip datayi daha etkili bir sekilde kullanabiliriz
# 5) slicing indexing kolay
# 6) time series data analizinde cok yardimci
# 7) ayrica herseyden onemlisi hiz pandas hiz acisindan optimize edilmis hizli bir kutuphane



dictionary = {"NAME":["ali","veli","kenan","hilal","ayse","evren"],
              "AGE":[15,16,17,33,45,66],
              "MAAS": [100,150,240,350,110,220]} 



dataFrame1 = pd.DataFrame(dictionary)# verileri tablo Åeklinde sÄ±ralÄ± bir Åekilde yazÄ±lÄ±yor
print(dataFrame1)


head = dataFrame1.head()#listeden ilk 5 satÄ±rÄ± alÄ±yor.  eÄer istersek iÃ§ine sayÄ± yazÄ±p istediÄimiz kadar satÄ±r alabiliriz
tail = dataFrame1.tail()#listeden son 5 sayÄ±yÄ± alÄ±yor. eÄer istersek iÃ§ine sayÄ± yazÄ±p istediÄimiz kadar satÄ±r alabiliriz
print(head)
print(tail)

#%% pandas basic methods

print(dataFrame1.columns)# tablodaki sutÃ¼nlarÄ±n baÅlÄ±klarÄ±nÄ± yazdÄ±rÄ±yor
print(dataFrame1.info()) # info tablo hakkÄ±nda detaylÄ± bilgi veriyor
print(dataFrame1.dtypes) # bu da hangi sutÃ¼nun tipini tek tek yazÄ±yor
print(dataFrame1.describe()) # tablo hakkÄ±nda ortalam, en az, en Ã§ok gibi numeric Åeyleri sÄ±ralar
#numeric feature = colums (age,maas)

#%% indexing and slicing

print(dataFrame1["AGE"])# sadece YaÅ sutÃ¼nu yazdÄ±r
print(dataFrame1.AGE) # bu da baÅka bir kullanÄ±m 
print(dataFrame1.NAME)

dataFrame1["yeni_feature"] = [-1,-2,-3,-4,-5,-6] # burada yeni bir sutÃ¼n oluÅturduk 

print(dataFrame1.loc[:,"AGE"]) # satÄ±rlarÄ±n hepsini al ama sutÃ¼nlardan AGE yi al

print(dataFrame1.loc[:3,"AGE"])#satÄ±rlardan 3. indexe kadar ve dahil olan satÄ±rlarÄ± alÄ±yor sutÃ¼nlardan ise AGE olanÄ± alÄ±yor

print(dataFrame1.loc[:3,"NAME":"yeni_feature"]) #satÄ±rlardan 3. indexe kadar sutÃ¼nlardan NAME'den yeni_feature kadar hepsini alÄ±yor

print(dataFrame1.loc[:3,["AGE","NAME"]]) # aynÄ± Åekilde bu sefer sutÃ¼nlardan sadece AGE ve NAME'i alÄ±yoruz
,
print(dataFrame1.loc[::-1,:]) # satÄ±rlarÄ± ters Ã§evir sutÃ¼nlarÄ±n hepsini yazdÄ±r

print(dataFrame1.loc[:,:"AGE"])# satÄ±rlarÄ±n hepsi sutÃ¼nlarÄ±n baÅtan AGE'ye olanlara kadar alÄ±yoruz

print(dataFrame1.loc[:,"NAME"])#isim sutÃ¼nunu yazdÄ±rdÄ±k 
print(dataFrame1.iloc[:,0])# burada ise iloc kullanarak index Åeklinde Ã§aÄÄ±rma iÅlemi yaptÄ±k



#%% filtering

filtre1 = dataFrame1.MAAS > 200

filtrelenmis_data = dataFrame1[filtre1] # bu Åekilde yapÄ±ldÄ±ÄÄ±nda koÅulu saÄlayanlar hepsi diÄer Ã¶zellikleri ile birlikte gelir
print(filtrelenmis_data)

filtre2 = dataFrame1.AGE <20 # bu Åekilde ise sadece bu sutÃ¼ndan true false deÄer dÃ¶ndÃ¼rÃ¼r
print(filtre2)

print(dataFrame1[filtre1 & filtre2]) #iki filtreyi bir arada toplayabiliriz

#ya da yukarÄ±daki gibi uzun bir Åekilde deÄilde aÅaÄÄ±daki gibi kÄ±sa bir Åekilde yapÄ±labilir
print(dataFrame1[dataFrame1.AGE > 60])


#%% list comprehestion 
import numpy as np

ortalama_maas = dataFrame1.MAAS.mean()
print(ortalama_maas) # bu pandas kullanÄ±mÄ± ile ortalama hesaplama

ortalama_maas1 = np.mean(dataFrame1.MAAS)
print(ortalama_maas1)# burada ise numpy ile ortalama hesapladÄ±k

dataFrame1["maas_seviyesi"] = ["DÃ¼ÅÃ¼k" if ortalama_maas > each else "yÃ¼ksek" for each in dataFrame1.MAAS]
"""
for each in dataFrame1.MAAS:
    if ortalama_maas > each:
        print("DÃ¼ÅÃ¼k")
    else:
        print("YÃ¼ksek")
        
YukarÄ±da tek satÄ±rda yazdÄÄ±mÄ±z kodun normal hali
"""

dataFrame1.columns
dataFrame1.columns = [each.lower() for each in dataFrame1.columns]# sutÃ¼nlarÄ± kÃ¼Ã§Ã¼k harfle yazdÄ±rdÄ±

#sutÃ¼nlarÄ±n kelimeler arasÄ±nda boÅluk varsa araya _ koyarak devam edilir
dataFrame1.columns = [eah.split()[0]+"_"+each.split()[1]  if(len(each.split())>1) else each  for each in dataFrame1.columns]

#%% drop and concatenating (bÄ±rakma ve birleÅtirme)

#dataFrame1.drop(["yeni_feature"],axis=1,inplace=True) #bu sutÃ¼nu kaldÄ±rÄ±yor tablodan

data1 = dataFrame1.head()
data2 = dataFrame1.tail()

#vertical (alt alta sÄ±ralama)
data_concat = pd.concat([data1,data2],axis=0)# iki Åeyi birleÅtirme 'concat'
print(data_concat)

#horizontal (yan yana sÄ±ralama)
maas = dataFrame1.maas
age = dataFrame1.age

data_h_concat = pd.concat([maas,age],axis=1)
print(data_h_concat)

#%% transforming data (verileri dÃ¶nÃ¼ÅtÃ¼rmek)

# tablodaki yaÅlarÄ± iki ile Ã§arpÄ±p daha sonra baÅka bir sutÃ¼n aÃ§arak oraya yazdÄ±k
dataFrame1["list_comp"] = [each*2 for each in dataFrame1.age]

#apply metotu
def multiply(age):
    return age*2

dataFrame1["apply_metotu"] = dataFrame1.age.apply(multiply)












