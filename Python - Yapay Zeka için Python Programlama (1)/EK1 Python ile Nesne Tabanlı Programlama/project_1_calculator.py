# calculator project
# class -> init -> method/attribute -> funct vs method

class Calc(object):
    "calculator"
    # init metodu
    def __init__(self, a, b):
        "initialize values"
        
        # attribute
        self.value1 = a
        self.value2 = b
    
    def add(self):
        "addition a+b = result -> return result"
        return self.value1 + self.value2
         
    def multiply(self):
        "multiplication a*b = result -> return result"
        return self.value1 * self.value2
    
    def division(self):
        "division a/b = result -> return result"
        return self.value1 / self.value2
           
print("Choose add(1), multiply(2), div(3)")
selection = input("select 1 or 2 or 3")

v1 = int(input("first value"))
v2 = int(input("second value"))

c1 = Calc(v1,v2)
if selection == "1":
    add_result = c1.add()
    print("Add: {}".format(add_result))
elif selection == "2": # else if = elif
    multiply_result = c1.multiply()
    print("Multiply: {}".format( multiply_result))
elif selection == "3":
    div_result = c1.division()
    print("Div: {}".format(div_result))
else: 
    print("Error there is no proper selection")
    
    
#%%



class calculator(object):
    
    def __init__(self, a,b):
        self.value1 = a
        self.value2 = b

    
    def add(self):
        return self.value1 + self.value2
        
    def multiply(self):
        return self.value1 * self.value2
    
    def division(self):
        return self.value1 / self.value2
    
    def extraction(self):
        return self.value1 - self.value2

    
while True:
    
    
    print("""
          1- Toplama işlemi
          2- Çarpma işlemi 
          3- Çıkarma işlemi
          4- Bölme işlemi 
          Çıkış yapmak için 0'a basınız...
          """)
    islem = input("Yapmak istediğiniz bir işlem seçiniz: ")
    
   
    
    if islem == "0":
        print("Uygulama çıkılıyor...")
        break
    
    elif(islem == "1"):
        value1 = int(input("Lütfen birinci sayıyı giriniz: "))
        value2 = int(input("Lütfen ikinci sayıyı giriniz: "))
        calc = calculator(value1, value2)
        result = calc.add()
        print("Toplamı: " , result)
    
    elif islem == "2":
        value1 = int(input("Lütfen birinci sayıyı giriniz: "))
        value2 = int(input("Lütfen ikinci sayıyı giriniz: "))
        calc = calculator(value1, value2)
        result = calc.multiply()
        print("Çarpımı: " , result)
        
    elif islem == "3":
        value1 = int(input("Lütfen birinci sayıyı giriniz: "))
        value2 = int(input("Lütfen ikinci sayıyı giriniz: "))
        calc = calculator(value1, value2)
        result = calc.extraction()
        print("Fark: " , result)
    
    elif islem == "4":
        value1 = int(input("Lütfen birinci sayıyı giriniz: "))
        value2 = int(input("Lütfen ikinci sayıyı giriniz: "))
        calc = calculator(value1, value2)
        result = calc.division()
        print("Bölüm: ", result)
    
    else: 
        print("Yanlış işlem yaptınız...")
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    