from django.db import models
from datetime import datetime


class Investment(models.Model):
    amount = models.FloatField(blank=False)
    timestamp = models.DateField(default=datetime.now)


    def __str_(self):
        return str(self.amount) + '  ' +  str(self.timestamp) 
 