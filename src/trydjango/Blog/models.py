from django.db import models

# Create your models here.
class Article(models.Model):
    Title = models.CharField(max_length=120)
    Description = models.TextField(blank=True,null=True)
    Summary = models.TextField(default='Nada')
    
