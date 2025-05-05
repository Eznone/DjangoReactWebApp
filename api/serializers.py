# requires rest_framework in django_rest_main
from rest_framework import serializers
from students.models import Student
from employees.models import Employee
from blogs.models import Blog, Comment

class StudentSerializer(serializers.ModelSerializer):
    # Must be called Meta so that framework finds the class
    class Meta:
        model = Student
        fields = "__all__"
        # fields = ['student_id', 'name', 'branch']

class EmployeeSerializer(serializers.ModelSerializer):
    # Must be called Meta so that framework finds the class
    class Meta:
        model = Employee
        fields = "__all__"
        # fields = ['emp_id', 'emp_name', 'designation']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Blog
        fields = '__all__'