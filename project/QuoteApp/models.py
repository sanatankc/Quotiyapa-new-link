from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.
class Quotes(models.Model):
    quotes = models.TextField()
    author = models.CharField(max_length=300)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

    def get_quotes(self):
        return self.quotes[:20] + " ..."
    def __unicode__(self):
        return self.quotes[:20] + " ..."
    class Meta:
        verbose_name = 'Quote'
        verbose_name_plural = 'Quotes'


class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    firstname =  models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    profile_picture = models.ImageField(upload_to='/static/images')