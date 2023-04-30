# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 07:41:44 2023

@author: Hasan Emre
"""
import numpy as np
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
#from wordcloud import WordCloud
import re
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import xgboost as xgb
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn import model_selection
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
#%%
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
sample = pd.read_csv("sample_submission.csv")


#%%
print(test.head(10))
print(train.head(10))
print(sample.head(10))

#%% shape of dataset
print(train.shape)
print(test.shape)

#%%
print(test.info())
print(train.info())

print(train.isna().sum())
print(test.isna().sum())

#%% drop location and keyword column
train.drop(["location","keyword"], axis = 1, inplace = True)
test.drop(["location","keyword"], axis = 1, inplace = True)


print(train.head())
print(test.head())

#%%
sns.countplot(x="target", data = train)
plt.show()
#%% 
len_train = train["text"].str.len()
len_test = test["text"].str.len()
plt.hist(len_train, label = "train tweets", alpha = 0.7, color = "blue")
plt.hist(len_test, label = "test tweets", alpha = 0.5, color = "red")
plt.legend()
plt.show()

#%% Data Cleaning

# cleaning the text

def cleaning_text(text):
    text = text.lower()
    text = re.sub("[^a-zA-Z]"," ", text)
    
    return text

train["text"] = train["text"].apply(lambda x: cleaning_text(x)) 
test["text"] = test["text"].apply(lambda x: cleaning_text(x)) 

print(train["text"].head(25))

#%%
tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
train["text"] = train["text"].apply(lambda x: tokenizer.tokenize(x))
test["text"] = test["text"].apply(lambda x: tokenizer.tokenize(x))

print(train["text"].head())
print(test["text"].head())
#%% Stopwords
nltk.download('stopwords')
nltk.download('omw-1.4')
nltk.download('wordnet')
nltk.download('punkt')
# stopwords
print(len(stopwords.words("english")))

#%%
# removing stopwords
def remove_stopwords(text):
    words = [word for word in text if word not in stopwords.words('english')]
    return words 
train['text'] = train['text'].apply(lambda x : remove_stopwords(x))
test['text'] = test['text'].apply(lambda x : remove_stopwords(x))

print(train.head())
print(test.head())

#%% Lemmatization

# lemmatization
lem = WordNetLemmatizer()
def lem_word(x):
    return [lem.lemmatize(w) for w in x]

#%% 
train['text'] = train['text'].apply(lem_word)
test['text'] = test['text'].apply(lem_word)
train['text'][:10]

#%% Takes a list of text and combines them into one large chunk of text.
def combine_text(ootext):
    combined_text = " ".join(ootext)
    return combined_text

train["text"] = train["text"].apply(lambda x: combine_text(x))
test["text"] = test["text"].apply(lambda x: combine_text(x))
train["text"]
print(train.head())

#%%  count vector

count_vector = CountVectorizer()
train_vector = count_vector.fit_transform(train["text"])
test_vector = count_vector.transform(test["text"])

print(train_vector[0].todense())

#%%
tfidf = TfidfVectorizer(min_df = 2,max_df = 0.5,ngram_range = (1,2))
train_tfidf = tfidf.fit_transform(train['text'])
test_tfidf = tfidf.transform(test['text'])

#%%
xgb_param = xgb.XGBClassifier(max_depth=5,n_estimators=500,colsample_bytree=0.8,nthread=10,learning_rate=0.05)

#%%

scores_vector = model_selection.cross_val_score(xgb_param,train_vector,train['target'],cv=5,scoring='f1')
print(scores_vector)
#%%

scores_tfidf = model_selection.cross_val_score(xgb_param,train_tfidf,train['target'],cv=5,scoring='f1')
print(scores_tfidf)

#%% 
xgb_param.get_params()

#%%
mnb = MultinomialNB(alpha = 2.0)
scores_vector = model_selection.cross_val_score(mnb,train_vector,train['target'],cv = 10,scoring = 'f1')
print("score:",scores_vector)
scores_tfidf = model_selection.cross_val_score(mnb,train_tfidf,train['target'],cv = 10,scoring = 'f1')
print("score of tfidf:",scores_tfidf)

#%%
mnb.get_params()
#%%
lg = LogisticRegression(C = 1.0)
scores_vector = model_selection.cross_val_score(lg, train_vector, train["target"], cv = 5, scoring = "f1")
print("score:",scores_vector)
scores_tfidf = model_selection.cross_val_score(lg, train_tfidf, train["target"], cv = 5, scoring = "f1")
print("score of tfidf:",scores_tfidf)

#%%
lg.get_params()

#%%
rf = RandomForestClassifier()
scores_vector = model_selection.cross_val_score(rf, train_vector, train["target"], cv = 5, scoring = "f1")
print("score:",scores_vector)
scores_tfidf = model_selection.cross_val_score(rf, train_tfidf, train["target"], cv = 5, scoring = "f1")
print("score of tfidf:",scores_tfidf)

#%%
dt = DecisionTreeClassifier()
scores_vector = model_selection.cross_val_score(dt, train_vector, train["target"], cv = 5, scoring = "f1")
print("score:",scores_vector)
scores_tfidf = model_selection.cross_val_score(dt, train_tfidf, train["target"], cv = 5, scoring = "f1")
print("score of tfidf:",scores_tfidf)

#%%
mnb.fit(train_tfidf, train["target"])
y_pred = mnb.predict(test_tfidf)

#%% Submission
disaster_tweets_df = pd.DataFrame({'Id':test['id'],'target':y_pred})

#%%
disaster_tweets_df.to_csv('disaster_tweets_df.csv',index=False)

#%%
disaster_tweets_df = pd.read_csv("disaster_tweets_df.csv")
print(disaster_tweets_df.head())














