from unicodedata import category
from django.db import models
# from rest_framework.validators import Uni
from django.utils import timezone
from torch import minimum

# Create your models here.
class Admin_User(models.Model):
    username = models.CharField(max_length=150, help_text=('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        
        error_messages={
            'unique': ("A user with that username already exists."),
        },
    )
    first_name = models.CharField( max_length=150, blank=True)
    last_name = models.CharField( max_length=150, blank=True)
    email = models.EmailField(unique=True, blank=False)
    is_staff = models.BooleanField( default=False,help_text=('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField( default=True, help_text=(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(default=timezone.now)
    password=models.CharField(max_length=16,blank=False)

class Book(models.Model):
    book_name=models.CharField(max_length=100)
    author=models.CharField(max_length=50)
    serial_no=models.CharField(max_length=20,unique=True)
    category=models.CharField(max_length=50)
    # class Meta:
    #     unique_together = ('book_name', 'author',)



