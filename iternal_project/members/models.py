from django.db import models

# Create your models here.
class UserCred(models.Model):
    emailID=models.EmailField(max_length = 254)
    contactNo=models.TextField(default='')
    username=models.TextField(max_length=50,default='')
    password=models.TextField(max_length=100,default='')
