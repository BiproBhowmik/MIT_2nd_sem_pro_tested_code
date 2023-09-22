from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers

import os
import openai

# from decouple import config

# OPENAI_API_KEY = config('OPENAI_API_KEY')

# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = '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'

# @login_required
def messegeResponse(request):
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}])
    print(completion.choices[0].message.content)
    return JsonResponse('chat_completion', safe=False)
