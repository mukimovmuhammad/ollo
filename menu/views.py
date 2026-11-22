from django.shortcuts import render
from .models import Dishes, Order, Category
from .serializers import OrderSerializer, DishesSerializer, CategorySerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

class OrderSetView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

class DishSetView(ModelViewSet):
    queryset = Dishes.objects.all()
    serializer_class = DishesSerializer
    permission_classes = [IsAuthenticated]

class CategorySetView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]