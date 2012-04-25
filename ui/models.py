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

class VoteRecord(models.Model):
    quote = models.ForeignKey(Quote)
    vote = models.IntegerField(default=0)
    ip4 = models.CharField(max_length=64)

    class Meta:
        unique_together = (
            ('quote', 'ip4'),
        )
