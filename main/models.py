from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    class Roles(models.TextChoices):
        BUYER = 'BUYER', 'buyer'
        SELLER = 'SELLER', 'seller'

    role = models.CharField(choices=Roles.choices, default=Roles.BUYER, max_length=50)

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.user.username


class Brands(models.Model):
    price = models.IntegerField(default=0, blank=False)
    condition = models.BooleanField(default=True, blank=False) # True: New , False: Used
    description = models.CharField(max_length=200, blank=True)
    
    class Meta:
        verbose_name_plural='Brands'
    def __str__(self):
        return self.name

    
class Make(models.Model):
    name=models.CharField(max_length=20,default='')
    image=models.ImageField(upload_to='phones/images',default='', blank=True)
    condition = models.BooleanField(default=True, blank=False) # True: New , False: Used
    color = models.CharField(max_length=50, blank=True)
    price=models.IntegerField(default=0)
    description=models.TextField(default='', blank=True)


    def __str__(self):
        return self.name