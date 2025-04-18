# requires rest_framework in django_rest_main
from rest_framework import serializers
from students.models import Student

class StudentSerializer(serializers.ModelSerializer):
    
    # Must be called Meta so that framework finds the class
    class Meta:
        model = Student
        fields = "__all__"
        # fields = ['student_id', 'name', 'branch']