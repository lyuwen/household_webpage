from __future__ import unicode_literals

from django.db import models
from datetime import datetime, date
from dateutil import tz

# Create your models here.

class Logs(models.Model):
    date=models.DateField(default=date.today())
    name=models.CharField(max_length=100)
    product=models.CharField(max_length=300)
    price=models.FloatField(default=0.)
    cleared=models.BooleanField(default=False)

    def __unicode__(self):              # __unicode__ on Python 2
        to_zone = tz.gettz('America/New_York')
        return "{}\t{}\t{}".format(self.date, self.name.strip().replace(' ','_'), self.price)
        #return "{}\t{}\t{}\t{:.2f}"%(self.date.astimezone(to_zone).strftime('%Y-%m-%d'), self.name, self.product, self.price)
class Pmt(models.Model):
    date=models.DateField(default=date.today())
    fromN=models.CharField(max_length=100)
    toN=models.CharField(max_length=100)
    amount=models.FloatField(default=0.)

    def __unicode__(self):              # __unicode__ on Python 2
        to_zone = tz.gettz('America/New_York')
        return "{}\t{}\t{}".format(self.date, self.fromN.strip().replace(' ','_'),  self.toN.strip().replace(' ','_'), self.amount)
        #return "{}\t{}\t{}\t{:.2f}"%(self.date.astimezone(to_zone).strftime('%Y-%m-%d'), self.name, self.product, self.amount)
