from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)

