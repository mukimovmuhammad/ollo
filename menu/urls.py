from django.urls import path
from . import views

urlpatterns = [
    path('dish/',views.DishSetView.as_view({'get': 'list'}),name='foods'),
    path('category/',views.CategorySetView.as_view({'get': 'list'}),name='categories'),
    path('order/',views.OrderSetView.as_view({'get': 'list'}), name='orders')
]
