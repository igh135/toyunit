from audioop import tomono

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from lunar.models import Lunar


class Vote(models.Model):
    vote_name = models.CharField(max_length=200)
    vote_cnt = models.IntegerField(default=0)
    elected = models.BooleanField()
    ongoing = models.BooleanField()

    class Meta:
        db_table = 'vote'
