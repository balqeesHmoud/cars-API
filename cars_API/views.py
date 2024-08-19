from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Car
from .serializers import CarSerializer
from .permissions import IsOwnerOrReadOnly

class CarListCreateView(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsOwnerOrReadOnly]
