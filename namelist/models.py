from django.db import models

# Create your models here.
class Namelist(models.Model):
    name_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=250)
