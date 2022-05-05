from django.db import models
class Userreg(models.Model):
    name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    uname=models.CharField(max_length=100)
    pwd=models.CharField(max_length=100)
    class Meta:
        db_table="newreg"