from django.db import models

class UserContacts(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile = models.CharField(max_length=50)
    message = models.TextField()