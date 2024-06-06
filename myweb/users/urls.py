from django.urls import path
from . import views, admin

app_name = 'users'

urlpatterns = [
    path('admin', admin.admin.site.urls),
    path('login/', views.login),
    path('logout/', views.logout),
]