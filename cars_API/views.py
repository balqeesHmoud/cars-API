from rest_framework import generics 
from .models import Car 
from serializer import CarSerializer

# ListCreateAPIView for listing and creating cars
class CarListCreateView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

# RetrieveUpdateDestroyAPIView for retrieving, updating, and deleting cars
class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
