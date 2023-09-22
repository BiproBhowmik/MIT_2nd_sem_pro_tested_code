# accounts/views.py
from django.contrib.auth.models import User
# from django.contrib.auth import authenticate

from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

# https://docs.djangoproject.com/en/4.2/topics/auth/default/

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponse("Log out")
    else:
        return HttpResponse('Not logged in')

def auth_user(request):
    if request.user.is_authenticated:
        username = request.user.username
        email = request.user.email
        # Access custom fields if you've added any
        # Example: bio = request.user.bio
        return HttpResponse(f'Username: {username}, Email: {email}')
    else:
        return HttpResponse('Not logged in')

def user_login(request):

    if request.method == 'POST':
        user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return HttpResponse("login")
        else:
            # No backend authenticated the credentials
            return HttpResponse("not login")
        


def user_register(request):
    
    if request.method == 'POST':
        # form = UserCreationForm(request.POST)
        user = User.objects.create_user(request.POST.get('username'), request.POST.get('email'), request.POST.get('password'))
        user.last_name = "Lennon"
        user.save()
        return HttpResponse(user)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # return redirect('dashboard')  # Replace 'dashboard' with the URL name for your dashboard or home page
            return JsonResponse(
            {
                'message': "Dashboard"
            }
        )
    else:
        form = UserCreationForm()
        return JsonResponse(
            {
                'message': "Not Registar"
            }
        )
