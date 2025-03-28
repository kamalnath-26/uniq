from django.db import models

# Create your models here.


class uniq(models.Model):
    PRODUCT_NAME=models.CharField(max_length=100)
    PRODUCT_CODE=models.CharField(max_length=100)
    PRICE=models.CharField(max_length=100)
    GST=models.CharField(max_length=100)
    FOODPRODECT=models.CharField(max_length=100)
