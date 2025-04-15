# requires rest_framework in django_rest_main
from rest_framework import serializers
from students.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        # fields = ['student_id', 'name', 'branch']