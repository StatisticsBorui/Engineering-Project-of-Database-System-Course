"""
URL configuration for myweb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from stu_page.views import student_page
from teacher_page.views import teacher_page
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path('student/', include('stu_page.urls')),
    path('teacher/', include('teacher_page.urls')),
    path('captcha/', include('captcha.urls')),
    path('user/', include('users.urls')),
    #path('something', index),
]

#设置静态文件路径
urlpatterns += staticfiles_urlpatterns()
