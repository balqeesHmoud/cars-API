from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Car(models.Model):
    model = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_bought = models.BooleanField(default=False)
    buyer = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    buy_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.model
    
      
    def get_absolute_url(self):
        return reverse("car_detail", args={self.id})
