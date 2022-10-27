from django.db import models

class About_Us(models.Model):
    title = models.CharField(max_length=50)
    title_head = models.TextField()
    title_desc = models.TextField()
