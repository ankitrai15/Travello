from django.db import models

class Dest(models.Model):
    dest_img = models.ImageField()
    dest_place = models.CharField(max_length=50)
    dest_desc = models.TextField()