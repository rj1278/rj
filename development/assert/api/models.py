from django.db import models

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
    