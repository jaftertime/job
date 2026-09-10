from django.db import models
class Table1(models.Model):
    name=models.CharField(max_length=20)
    age=models.IntegerField()
    height=models.FloatField()
