from django.db import models


# Create your models here.

class Shopping(models.Model):
    pid = models.CharField(max_length=200)
    itemName = models.CharField(max_length=300)
    perItemPrice = models.CharField(max_length=100)
    totalQuantity = models.CharField(max_length=100)


class Meta:
    db_table = "shopping"
