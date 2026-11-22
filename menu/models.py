from django.db import models
from accounts.models import CustomUser

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Dishes(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="dishes")

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="orders")
    dishes = models.ManyToManyField(Dishes,related_name="orders")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)