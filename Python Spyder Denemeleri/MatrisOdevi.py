import numpy as np

while(True):
    
    print("""
          
          MATRİSLER İLE İŞLEMLER
          
          1-Matrislerle toplama işlemi\n
          2-Matrislerle çıkarma işlemi\n
          3-Matrislerle çarpma işlemi\n
          4-Matrisin sabit sayı ile çarpımı\n
          5-Matrisin determinatını hesapalama \n
          6-Matrisin tersini alma\n
          7-Matrisin involutif matris olup olmadığını belirleme\n
          Çıkış yapmak için 0'a basınız...
          
          """)
          
    islem = input("Yapmak istediğiniz bir işlem seçiniz: ")

    
    if(islem == "0"):
        print("Sistemden çıkılyor...")
        break
  
    elif(islem == "1"):
        
        print("\nBirinci matrisinin satır ve sutün sayılarını giriniz...")
        row = int(input("Birinci matrisin satır sayısını giriniz: "))
        col = int(input("İkinci matrisin sutün sayısını giriniz: "))
        
        matris1 = np.random.randint(20,size=(row,col))
        print()
        print(matris1,"\n")
        
        print("\nİkinci matrisin satır ve sutün sayılarını giriniz...")
        row1 = int(input("Birinci matrisin satır sayısını giriniz: "))
        col1 = int(input("İkinci matrisin sutün sayısını giriniz: "))
        
        if(row == row1  and  col == col1):
            
            matris2 = np.random.randint(20,size=(row1,col1))
            print()
            print(matris2)
            print("\n")
            print("Toplama işlemi sonucu...\n")
            print(matris1+matris2,"\n")
            
        else:
            print("\nToplama işleminde iki matrisinde satır ve sutünlar eşit olmalıdır...")
           
        
    elif(islem == "2"):
        print("\nBirinci matrisinin satır ve sutün sayılarını giriniz...")
        row = int(input("Birinci matrisin satır sayısını giriniz: "))
        col = int(input("İkinci matrisin sutün sayısını giriniz: "))
        
        matris1 = np.random.randint(20,size=(row,col))
        print()
        
        print(matris1,"\n")
        
        print("\nİkinci matrisin satır ve sutün sayılarını giriniz...")
        row1 = int(input("Birinci matrisin satır sayısını giriniz: "))
        col1 = int(input("İkinci matrisin sutün sayısını giriniz: "))
        
        if(row == row1  and  col == col1):
            
            matris2 = np.random.randint(20,size=(row1,col1))
            print()
            print(matris2)
            print("\n")
            print("Çıkarma işlemi sonucu...\n")
            print(matris1-matris2,"\n")
            
        else:
            print("\nÇıkarma işleminde iki matrisinde satır ve sutünlar eşit olmalıdır...")
      
    elif(islem == "3"):
        print("\nBirinci matrisinin satır ve sutün sayılarını giriniz...")
        row = int(input("Birinci matrisin satır sayısını giriniz: "))
        col = int(input("İkinci matrisin sutün sayısını giriniz: "))
        
        matris1 = np.random.randint(20,size=(row,col))
        print()
        
        print(matris1,"\n")
        
        print("\nİkinci matrisin satır ve sutün sayılarını giriniz...")
        row1 = int(input("Birinci matrisin satır sayısını giriniz: "))
        col1 = int(input("İkinci matrisin sutün sayısını giriniz: "))
        
        if(col == row1):
            
            matris2 = np.random.randint(20,size=(row1,col1))
            print()
            print(matris2)
            print("\n")
            print("Çarpma işlemi sonucu...\n")
            
            print(matris1.dot(matris2))
            
        else:
            print("\nÇarpma işleminde birinci matrisin sutün sayısı ile ikinci matrisin satır sayısı aynı olmalıdır...")
        
            
    elif(islem == "4"):
        print("\nBirinci matrisinin satır ve sutün sayılarını giriniz...")
        row = int(input("Birinci matrisin satır sayısını giriniz: "))
        col = int(input("İkinci matrisin sutün sayısını giriniz: "))
        
        matris1 = np.random.randint(20,size=(row,col))
        print()       
        print(matris1,"\n")      
        sayi = int(input("Matrisi çarpmak istediğiniz sabit sayıyı giriniz: "))        
        print(matris1*sayi)
        
        
    elif(islem == "5"):
        print("\nBirinci matrisinin satır ve sutün sayılarını giriniz...")
        row = int(input("Birinci matrisin satır sayısını giriniz: "))
        col = int(input("İkinci matrisin sutün sayısını giriniz: "))
        if(col == row):
            matris1 = np.random.randint(20,size=(row,col))
            print()       
            print(matris1,"\n")
            print("Matrisin determinatı: ",np.linalg.det(matris1))
        else:
            print("\nDeterminatını alabilmek için matris kare matris olmalıdır...")
            
               
    elif(islem == "6"):
        print("\nBirinci matrisinin satır ve sutün sayılarını giriniz...")
        row = int(input("Birinci matrisin satır sayısını giriniz: "))
        col = int(input("İkinci matrisin sutün sayısını giriniz: "))
        if(col == row):
            matris1 = np.random.randint(20,size=(row,col))
            print()       
            print(matris1,"\n")
            print(np.linalg.inv(matris1))
        else:
            print("\nTersini alabilmek için matrisin kare matris olmalıdır...")
               
        
    elif(islem == "7"):
        print("\nBirinci matrisinin satır ve sutün sayılarını giriniz...")
        row = int(input("Birinci matrisin satır sayısını giriniz: "))
        col = int(input("İkinci matrisin sutün sayısını giriniz: "))
        if(col == row):
            matris1 = np.random.randint(20,size=(row,col))
            print()       
            print(matris1,"\n")
            matris2 = np.dot(matris1, matris1)
            birimMatris = np.eye(row)
            if(matris2.all == birimMatris.all):
                print("\nİnvolutif matrsidir\n",matris2)
            else:
                print("\nİnvolutif matris değildir...")
                
        else:
            print("Matrisin involutif matris olup olamdığüını kabul etmek için kare matris olması gerekir...")
           
    else:
         print("Yanlış işlem girdiniz lütfen tekrar deneyiniz...")