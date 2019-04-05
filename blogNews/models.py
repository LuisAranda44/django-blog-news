import os
from django.db import models
from django.dispatch import receiver

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
    image = models.ImageField(upload_to='news', blank="True", default="descarga.jpg")

def _delete_file(path):
    """ Deletes file from filesystem. """
    if os.path.isfile(path):
            os.remove(path)

@receiver(models.signals.post_delete, sender=New)
def delete_file(sender, instance, *args, **kwargs):
    """ Deletes image files on `post_delete` """
    if instance.image:
        _delete_file(instance.image.path)


    # def publish(self):
    #     self.published_date = timezone.now()
    #     self.save()

