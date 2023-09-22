from django.http import JsonResponse
from django.shortcuts import render

import pandas as pd

def pricePredict(request):
    if request.method == 'POST':
        w_kg = request.POST.get('w_kg')
        w_kg = float(w_kg)
        # print(type(w_kg))

        # return JsonResponse({'result': w_kg},safe=False)
    
        model = pd.read_pickle(r"./prediction_model2.pickle")
        result = model.predict([[w_kg]])

        classification = result[0]

        return JsonResponse({'result': classification,},safe=False)

