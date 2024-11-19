from django.urls import path
from . import views

urlpatterns = [
    path('admin/generate-nested/', views.generate_nested, name='generate_nested'),
    path('admin/generate-nested2/', views.generate_nested2, name='generate_nested2'),
]
