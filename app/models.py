from django.db import models

# Create your models here.
class User(models.Model):
    id  = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    phoneNumber = models.IntegerField()
    pinCode = models.IntegerField()

class Symptoms(models.Model):
    userId = models.ForeignKey(User, on_delete=models.PROTECT)
    travelHistory = models.BooleanField()
    contactWithCovidPatient = models.BooleanField()
    symptoms = models.CharField(max_length=256)
    riskPercentage = models.IntegerField(default=0)

class Admin(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    phoneNumber = models.IntegerField()
    pinCode = models.IntegerField()

class CovidResult(models.Model):
    userId = models.ForeignKey(User, on_delete=models.PROTECT)
    adminId = models.ForeignKey(Admin, on_delete=models.PROTECT)
    result = models.CharField(max_length=20, default='negative')
