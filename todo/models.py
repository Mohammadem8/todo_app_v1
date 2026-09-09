from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):

    user = models.ForeignKey(User , on_delete=models.CASCADE , null=True)
    task = models.CharField(max_length=250)
    status = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)

