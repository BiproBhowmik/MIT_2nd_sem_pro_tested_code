from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers

from crud.models import Employee

@login_required
def read(request):
    employees = Employee.objects.all()
    data = serializers.serialize('json', employees)  # Convert the queryset to JSON data
    return JsonResponse(data, safe=False)

@login_required
def create(request):
    if request.method == 'POST':
        item1 = Employee(
            name = request.POST.get('name')
        )
    
        item1.save()

        return JsonResponse(
            {
                'message': "Inserted"
            }
        )
    else:
        return JsonResponse(
            {
                'message': "Post request is accepted fount other"
            }
        )

@login_required
def update(request):
    e_id = request.POST.get('id')
    employee_to_update = Employee.objects.get(pk=e_id)  # Replace '1' with the primary key of the employee you want to update

    employee_to_update.name = request.POST.get('name')
    employee_to_update.save()

    data = Employee.objects.get(id=e_id)
    employee_object = serializers.serialize('json', [data])

    return JsonResponse(
            {
                'message': "Updated",
                'updated_data': employee_object,
            },
            safe=False
        )

from .models import Employee

@login_required
def delete(request):
    e_id = request.POST.get('id')
    try:
        # Retrieve the employee with the specified ID
        employee = Employee.objects.get(id=e_id)

        # Delete the employee
        employee.delete()

        return JsonResponse({'message': 'Employee deleted'})

    except Employee.DoesNotExist:
        # Handle the case where the employee with the specified ID does not exist
        return JsonResponse({'error': 'Employee not found'}, status=404)
