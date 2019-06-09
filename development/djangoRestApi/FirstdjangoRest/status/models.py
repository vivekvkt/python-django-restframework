from django.db import models
import json
from django.conf import settings
from django.db import models
# Create your models here.

def upload_update_image(instance, filename):
    return "updates/{user}/{filename}".format(user= instance.user, filename=filename)

class StatusQuerySet(models.QuerySet):
    pass


class StatusManager(models.Manager):
    def get_queryset(self):
        return StatusQuerySet(self.model,  using=self._db)


class Status(models.Model):
    user        = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content     = models.TextField(blank=True, null=True)
    image       = models.ImageField(upload_to=upload_update_image, blank=True, null= True)
    Updated     = models.DateTimeField(auto_now_add=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)[:50]

class Meta:
    verbose_name = 'Status post'
    verbose_name_plural = 'Status posts'