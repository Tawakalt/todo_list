from django.db import models

# Create your models here.
class Token(models.Model):
    email = models.EmailField()
    uid = models.CharField(max_length=255)
