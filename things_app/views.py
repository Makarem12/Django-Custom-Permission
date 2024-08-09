from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializer import carsSerializer
from .models import Car
from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import IsOwnerOrReadOnly

class carsList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class= carsSerializer
    permission_classes=[IsAuthenticated]

class carDetails(generics.RetrieveUpdateDestroyAPIView):
        queryset = Car.objects.all()
        serializer_class= carsSerializer
        permission_classes=[IsOwnerOrReadOnly]