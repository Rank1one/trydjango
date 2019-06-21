from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    Title = models.CharField(max_length=120)
    Price = models.DecimalField(default=0.00,decimal_places=2,max_digits=65)
    Description = models.TextField(blank=True,null=True)
    Summary = models.TextField(default='Nada')
    Soldout = models.BooleanField()

    def get_absolute_url(self):
        # return f"/product/{self.id}"
        return reverse("products:dynamic_pview",kwargs={'my_id': self.id})