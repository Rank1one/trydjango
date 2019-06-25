from django.db import models
from django.urls import reverse

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(default='Write a content')
    active = models.BooleanField(default=True)
    
    def get_absolute_url(self):
        return reverse("Blog:article-details",kwargs={'id': self.id})