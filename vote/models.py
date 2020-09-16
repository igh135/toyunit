from audioop import tomono

from django.db import models

# Create your models here.
from self import self

import user
from lunar.models import Lunar
from user.models import User


class Vote(models.Model):
    vote_name = models.CharField(max_length=200)
    vote_cnt = models.IntegerField(default=0)
    elected = models.BooleanField()
    ongoing = models.BooleanField()
    UserID = models.ForeignKey(to=User, related_name='user_id', on_delete=models.CASCADE)
    name = models.ForeignKey(to=User,on_delete=models.CASCADE)
    class Meta:
        db_table = 'vote'
