from django.urls import path
from . import views

urlpatterns = [
    path('admin/generate-nested/', views.generate_nested, name='generate_nested'),
]
