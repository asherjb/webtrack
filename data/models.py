from django.db import models

# Create your models here.

class Entry(models.Model):
    value = models.DecimalField(max_digits=10, decimal_places = 3)
    unit = models.CharField(max_length=200)
    entry_date = models.DateTimeField('date entered')

