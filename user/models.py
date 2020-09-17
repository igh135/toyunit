from django.db import models


# Create your models here.
class User(models.Model):
    UserID = models.CharField(max_length=15)
    password = models.CharField(max_length=25)
    name = models.CharField(max_length=20)
    authority = models.BooleanField(default=False)

    class Meta:
        db_table = 'user'

