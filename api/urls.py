from django.urls import path
from django import views

urlpatterns = [
    path('students/', views.studentsView),
]