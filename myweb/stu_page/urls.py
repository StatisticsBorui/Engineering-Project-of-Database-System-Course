from django.urls import path
from . import views

app_name = 'stu_page'

urlpatterns = [
    path('', views.student_page),
]