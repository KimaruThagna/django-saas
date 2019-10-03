from django.db import models
from datetime import  datetime
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
import random,string
from .validators import *
# Create your models here.
def requestNumGenerator():
    return ''.join(random.choice(string.ascii_uppercase + string.digits+string.ascii_lowercase) for _ in range(10))


class PatientData(models.Model):
    requestNumber=models.CharField(max_length=200,unique=True,default=requestNumGenerator)
    patient_num=models.CharField(max_length=200)
    requestDate=models.DateTimeField(default=timezone.now())
    requestingPractitioner=models.ForeignKey(User,on_delete=models.CASCADE)
    medical_Image=models.ImageField(upload_to='medical')
    #validators = [validate_file_shape, validate_file_extension]
    processed=models.BooleanField(default=False)
    lastUpdated = models.DateTimeField(auto_now=True, auto_now_add=False)
    addedOn = models.DateTimeField(default=timezone.now())

    class Meta:
        verbose_name_plural='Patients data'
    def __str__(self):
        return self.requestNumber
