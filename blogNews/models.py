from django.contrib import admin
from django.db import models

from django.utils import timezone

# Create your models here.
class BaseItems(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    body = models.TextField()
    class Meta:
        abstract=True

    def __str__(self):
        return self.title

class New(BaseItems):
    published_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='news',blank="False",default="/home/laranda/Descargas/coche.jpeg")


    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()
