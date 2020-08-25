from audioop import tomono

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Vote(models.Model):
    vote_name = models.CharField(max_length=200)
    vote_cnt = models.IntegerField(default=0)
    elected = models.BooleanField()
    ongoing = models.BooleanField()
    UserID = models.ForeignKey(User, related_name='UserID', on_delete=models.CASCADE)
    name = models.ForeignKey(User, related_name='name', on_delete=models.CASCADE)

    class Meta:
        db_table = 'vote'
