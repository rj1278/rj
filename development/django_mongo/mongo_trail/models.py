from django.db import models

# Create your models here.
from django.db import models
from django.db.models.base import Model

# Create your models here.
class Student(models.Model): 
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    grade = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name

class FileUpload(models.Model):
    file=models.FileField(null=False,blank=False)
    des=models.CharField(max_length=20)
    timestamp=models.DateTimeField(auto_now_add=True)

class TestTable(models.Model):
    name=models.CharField(max_length=20)

class Members(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    created_date=models.DateTimeField(auto_now_add=True)
class Assets(models.Model):
    asset_name=models.CharField(max_length=30)
    total_count=models.IntegerField()
    current_count=models.IntegerField()
    created_date=models.DateTimeField(auto_now_add=True)

class Member_Assets(models.Model):
    member=models.ForeignKey(Members,on_delete=models.PROTECT)
    asset=models.ForeignKey(Assets,on_delete=models.PROTECT)
    message=models.CharField(max_length=200)