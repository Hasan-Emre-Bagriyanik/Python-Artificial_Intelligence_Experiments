# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 07:15:41 2023

@author: Hasan Emre
"""



import pandas as pd


#%% import twitter data

data = pd.read_csv("gender_classifier.csv", encoding="latin1")
data = pd.concat([data.gender, data.description], axis = 1)
data.dropna(axis = 0,inplace = True)
data.gender = [1 if i == "female" else 0 for i in data.gender]


#%% cleaning data
# Regular expression RE mesala "[^a-zA-Z]" 

import re

first_description = data.description[4]
# a'dan z ye ve A dan Z ye  kadar olan harfleri bulma geri kalanlari " " (space) ile degistir
description = re.sub("[^a-zA-Z]", " ", first_description)

# Buyuk harften kucuk harfe cevirme
description = description.lower()   

#%% stopwords   (irrelavent words)  gereksiz kelimeler
import nltk   # natural language tool kit
nltk.download("wordnet")  # carpus diye bir klasore indiriliyor
nltk.download("stopwords")  # tokenize icin 
nltk.download('omw-1.4')   # lemma icin
from nltk.corpus import stopwords  # sonra ben corpus klasorunden import ediyorum

#description = description.split()

# split yerine tokenizer kullanabiliriz
description = nltk.word_tokenize(description)

# split kullanirsak "shouldn't " gibi kelimler "should" ve "not" diye ikiye ayrılmaz ama word_tokenize ile ayrılır
#%%
# gereksiz kelimeleri cikar
description = [word for word in description if not word in set(stopwords.words("english"))]

#%%  lemmatazation   loved -> love   gitmeyecegim -> git   burada kelimelerin koklerini bulmaya calisacagiz

import nltk as nlp

lemma = nlp.WordNetLemmatizer()
description = [lemma.lemmatize(word) for word in description]

# cumleyi bosluk ile birlestirme yapiyoruz
description = " ".join(description)

#%%   suana kadar sadece bir description icin yapmistik simdi ise tumunde yapmak

description_list = []

for description in data.description:
    description = re.sub("[^a-zA-Z]", " ", description)
    description = description.lower() 
    description = nltk.word_tokenize(description)
    #description = [word for word in description if not word in set(stopwords.words("english"))]
    lemma = nlp.WordNetLemmatizer()
    description = [lemma .lemmatize(word) for word in description]
    description = " ".join(description)
    description_list.append(description)


#%%  bag of words
# bag of word yaratmak icin kullandigim metot
from sklearn.feature_extraction.text import CountVectorizer
max_features = 15000

# lowercase()  ile burda kelimeleri kucuk harfe cevirebiliriz
# token_pattern()  ile gereksiz kelimeleri cikarabiliriz
count_vectorizer = CountVectorizer(max_features = max_features, stop_words="english")

# kelimeleri sikliklarina gore 0 ve 1 lere cevirdik
sparce_matrix = count_vectorizer.fit_transform(description_list).toarray()

print("En sık Kullanılan  {} kelimeler : {} ".format(max_features, count_vectorizer.get_feature_names()))

#%% 

y = data.iloc[:,0].values   # male or female classes
x = sparce_matrix

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 0)

#%% # Fitting Logistic Regression to the Training set
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(random_state = 0)
classifier.fit(x_train, y_train)

#%% Predicting the Test set results
y_pred = classifier.predict(x_test)

#%% Making the Confusion Matrix
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
acc_score = accuracy_score(y_test, y_pred)
print(acc_score*100)
print(cm)

