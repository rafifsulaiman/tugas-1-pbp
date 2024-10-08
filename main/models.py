from django.db import models
import uuid
from django.contrib.auth.models import User

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    price = models.IntegerField()
    description = models.TextField(max_length=300)
    image = models.URLField(max_length=500)