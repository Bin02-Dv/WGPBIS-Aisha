from django.urls import path
from . import views

urlpatterns = [
    path('dash/', views.dash, name="dash"),
    path('inventory/', views.inventory, name='inventory')
]
