from django.urls import path
from .views import CarListCreateView, CarDetailView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('cars/', CarListCreateView.as_view(), name='api_car_lis'),
    path('cars/<int:pk>/', CarDetailView.as_view(), name='car-detail'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


]
