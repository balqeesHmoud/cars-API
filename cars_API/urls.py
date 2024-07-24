from django.urls import path
from .views import CarListCreateView, CarDetailView

urlpatterns = [
    path('cars/', CarListCreateView.as_view(), name='api_car_lis'),
    path('cars/<int:pk>/', CarDetailView.as_view(), name='car-detail'),
]
