from django.urls import path

from . import views

app_name = 'teacher_page'

urlpatterns = [
    path('page', views.teacher_page),
    path('insert', views.insert_data),
    path('delete', views.delete_data),
    path('upload', views.upload_result),
]