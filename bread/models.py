from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

class Bread(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(default="")
    bread_type = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('bread-detail', kwargs={'id': self.id})
