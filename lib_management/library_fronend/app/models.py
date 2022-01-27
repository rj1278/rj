from django.db import models

# Create your models here.

class GetUser:
    def __init__(self):
        self.email=None
    def set_email(self,email):
        self.email=email
    def get_email(self):
        return self.email
        