from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class getUserList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    active_time = models.BigIntegerField(null=True)

