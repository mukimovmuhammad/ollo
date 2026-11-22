from rest_framework import serializers
from .models import Category,Dishes,Order

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class DishesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dishes
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ["user"]
