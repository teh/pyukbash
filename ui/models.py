import datetime 
from django.db import models

class Quote(models.Model):
    text = models.TextField()
    created = models.DateTimeField(default=datetime.datetime.utcnow)

    up = models.IntegerField()
    down = models.IntegerField()