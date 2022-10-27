from django.db import models
from django.db.models.base import Model

class HomeImage(models.Model):
    home_img = models.ImageField()