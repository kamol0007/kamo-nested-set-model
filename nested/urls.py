from django.urls import path
from . import views

urlpatterns = [
    path('admin/nested-set-model/<str:app_name>/<str:model_name>', views.generate_nested, name='set_nested_model'),
]
