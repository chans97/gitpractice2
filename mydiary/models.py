from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.
class Content(models.Model):
    # objects = models.Manager()
    title = models.CharField(max_length=200, null=True)
    user = models.CharField(max_length=200, null=True)
    pub_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(
        upload_to=None, height_field=None, width_field=None, max_length=None, null=True
    )
    star = models.IntegerField(null=True)
    highlight = models.CharField(max_length=200, null=True)
    review = models.TextField(default="", null=True)
