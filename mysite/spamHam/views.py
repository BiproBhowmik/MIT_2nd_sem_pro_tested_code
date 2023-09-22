from django.http import JsonResponse
from django.shortcuts import render

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.naive_bayes import MultinomialNB

import pickle
import joblib

import numpy as np

def emailPredict(request):
    if request.method == 'POST':
        data = pd.read_csv("./emails.csv")

        # print(data.shape)

        X = data['text'].values
        y = data['spam'].values

        # print(X)
        # print(y)

        X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2 , random_state= 0)

        cv = CountVectorizer()
        x_train = cv.fit_transform(X_train)

        # print(x_train.shape)

        nb = MultinomialNB()

        nb.fit(x_train, y_train)

        x_test = cv.transform(X_test)

        # print(x_test.shape)

        y_pred = nb.predict(x_test)

        # print(accuracy_score(y_pred, y_test))

        # print(nb.score(x_train,y_train))

        email = [request.POST.get('email')]

        clean_email = cv.transform(email)

        check = nb.predict(clean_email)[0]

        mailType = ""

        if check == 0:
            print("This is a Ham Email!")
            mailType = 'This is a Ham Email!'
        else:
            print("This is a Spam Email!")
            mailType = 'This is a Spam Email!'

        return JsonResponse({'result': mailType,},safe=False)

        
# def emailPredict(request):
#     if request.method == 'POST':
#         # email = request.POST.get('email')
#         # w_kg = float(w_kg)
#         # print(type(email))

#         model = pd.read_pickle(r"./shpred.pickle")

#         email = ['Hey i am Joy. How are you?']
 
#         # Create a Vectorizer Object
#         vectorizer = CountVectorizer()
        
#         vectorizer.fit(email)
        
#         # Printing the identified Unique words along with their indices
#         print("Vocabulary: ", vectorizer.vocabulary_)
        
#         # Encode the Document
#         vector = vectorizer.transform(email)
        
#         # Summarizing the Encoded Texts
#         print("Encoded Document is:")
#         print(vector.toarray())
#         print("Encoded vector:")
#         print(vector)



        
#         # result = model.predict(vector)[0]

#         print("Input Data Shape:", vector.shape)
#         print("Model's Feature Count:", model.feature_count_.shape)  # Adjust based on your model attributes

#         return JsonResponse({'result': 'classification',},safe=False)
