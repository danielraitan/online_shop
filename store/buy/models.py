from django.db import models

class ItemInfo(models.Model):
    item_image = models.URLField()
    item_name = models.CharField(max_length=50)
    item_color = models.CharField(max_length=50)
    type = models.CharField(max_length=50)    
    size = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=9, decimal_places=0)
    
    def __str__(self):
        return f'{self.item_name}, {self.price}'
    
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return f'{self.first_name}, {self.last_name}'
    
class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.username}'
    

# Create your models here.
