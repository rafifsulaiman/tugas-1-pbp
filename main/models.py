from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField()
    description = models.TextField(max_length=300)
    image = models.ImageField() #upload image
    person_name = models.CharField(max_length=300)
    person_class = models.TextField()
    person_npm = models.IntegerField()