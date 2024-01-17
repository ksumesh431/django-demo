# myapp/urls.py
from django.urls import path
from .views import index, welcome

urlpatterns = [
    path('', index, name='index'),
    path('welcome/<int:pk>/', welcome, name='welcome'),
]
