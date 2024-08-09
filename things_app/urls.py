from django.contrib import admin

from django.urls import path
from .views import carsList ,carDetails

urlpatterns = [
    
    path('', carsList.as_view(), name='cars_list'),
    path('<int:pk>/', carDetails.as_view(), name="car_details"),
   
]