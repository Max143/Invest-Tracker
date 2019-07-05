from django.db import models
from datetime import datetime
from django.contrib.auth.models import User





class Investor(models.Model):  
    name = models.CharField(max_length=99) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name


class Investment(models.Model):
    amount = models.FloatField(blank=False)
    rate = models.FloatField(blank=False)
    timestamp = models.DateField(default=datetime.now)
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.investor)