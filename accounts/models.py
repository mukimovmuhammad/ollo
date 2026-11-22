from django.contrib.auth.models import AbstractUser
from django.db.models import * 

class CustomUser(AbstractUser):
    ROLE_USER = [
        ('client','Client'),
        ('ceo',"CEO")
    ]
    
    role = CharField(choices=ROLE_USER)
    def __str__(self):
        return self.username
