from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def home(request):
    data = 'Employee'
    return HttpResponse(data)

def profile(request):
    return render(request, 'employee/profile.html')

def insertdata(request):
    if request.method == 'POST':
        data = {
        'name': request.POST.get('username'),
        'age': 30,
        'city': 'New York',
    }
        return JsonResponse(data)
    else:
        return render(request, 'post_form.html')
