from django.db import models
from datetime import datetime

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='products')
    active = models.BooleanField(default=True)
    created_at = models.DateField(default=datetime.now)

    def __str__(self):
        return self.name
