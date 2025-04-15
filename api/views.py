# from django.shortcuts import render
# from django.http import JsonResponse
from students.models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Without api_view we dont get the cool UI
@api_view(['GET'])
def studentsView(request):
    if request.method == 'GET':
        # Get all data from Student table
        students = Student.objects.all()
        # Many makes it so we fetch various students
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)