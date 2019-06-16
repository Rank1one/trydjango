from django.db import models

# Create your models here.
class Product(models.Model):
    Title = models.CharField(max_length=120)
    Price = models.DecimalField(default=0.00,decimal_places=2,max_digits=100)
    Description = models.TextField(blank=True,null=True)
    Summary = models.TextField()