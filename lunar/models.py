from django.db import models

# Create your models here.
from user.models import User


class Lunar(models.Model):
    name = models.CharField(max_length=15)
    prof_img = models.ImageField(max_length=100)
    class Meta:
        db_table = 'lunar'
