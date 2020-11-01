from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
    total = models.FloatField(default=0)
    total_in = models.FloatField(default=0)
    total_ex = models.FloatField(default=0)

    def __str__(self):
        return self.username


class Transaction(models.Model):
    trans_id = models.CharField(max_length=255)
    account_id = models.ForeignKey(Account, related_name='history_trans',on_delete=models.CASCADE)
    TYPE_CHOICE = [
        ('IN','Income'),
        ('EX','Expense')
    ]
    type = models.CharField(max_length=2,choices=TYPE_CHOICE,blank=False)
    value = models.FloatField(blank=False)
    date = models.DateTimeField(auto_now_add=True)
    ps = models.CharField(max_length=255,blank=True)
    def __str__(self):
        return "{} {}".format(self.type,self.value)
    