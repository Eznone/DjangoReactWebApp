from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def studentsView(request):
    students = {
        'id': 1,
        'name': 'Enzo',
        'class': 'Software Engineering'
    }
    return JsonResponse(students)