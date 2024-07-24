from rest_framework import serializers
from .models import Car

class CarSerializer(serializers.ModelSerializer):
    buy_time = serializers.SerializerMethodField()
    class Meta:
        model = Car
        fields = '__all__'


    def get_buy_time(self, obj):
        return obj.buy_time.date() if obj.buy_time else None
