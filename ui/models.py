import datetime 
from django.db import models

class Quote(models.Model):
    text = models.TextField()
    created = models.DateTimeField(default=datetime.datetime.utcnow)

    up = models.IntegerField(default=0)
    down = models.IntegerField(default=0)

    def total(self):
        return self.up - self.down

    def __unicode__(self):
        return self.text[:100]
