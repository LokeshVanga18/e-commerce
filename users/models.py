from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=10)
    address = models.CharField(max_length=200)