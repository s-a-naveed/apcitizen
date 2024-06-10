from django.db import models

# Create your models here.
class commoninfo(models.Model):
    full_name = models.CharField(max_length=50)
    aadhar_number = models.IntegerField(unique=True, null=False)
    class Meta:
        abstract = True
class aadhar(commoninfo):
    date_of_birth = models.DateField()
    father_name = models.CharField(max_length=50)
    phone_number = models.IntegerField()
    address = models.CharField(max_length=100)
    
class voterregister(commoninfo):
    user_name = models.CharField(max_length=30, unique=True, null=False)
    password = models.CharField(max_length=30)
    full_name = None

class mlapolling(models.Model):
    user = models.IntegerField(unique=True)
    MLA_name = models.CharField(max_length=50)
    
class mppolling(models.Model):
    user = models.IntegerField(unique=True)
    MP_name = models.CharField(max_length=50)