from django.db import models

# Create your models here.

class doctor_details(models.Model):
    name=models.CharField(max_length=200)
    level=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    dt = models.DateField(auto_now_add=True)
    tm = models.TimeField(auto_now_add=True)
    status = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Patient_details(models.Model):
    doctor_name = models.ForeignKey(doctor_details,related_name="doc_details", on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=50)
    address=models.TextField(max_length=500)
    email=models.EmailField(max_length=200)
    mobile=models.CharField(max_length=200)
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
    dt = models.DateField(auto_now_add=True)
    tm = models.TimeField(auto_now_add=True)
    status = models.CharField(max_length=255)


    def __str__(self):
        return self.patient_name


class Prediction_details_new(models.Model):
    doctor_name=models.ForeignKey(doctor_details,on_delete=models.CASCADE ,related_name="prediction1")
    patient_name=models.ForeignKey(Patient_details,on_delete=models.CASCADE ,related_name="patient1")
    erythema=models.CharField(max_length=200)
    saw_tooth=models.CharField(max_length=200)
    scaling=models.CharField(max_length=200)
    itching=models.CharField(max_length=200)
    melanin=models.CharField(max_length=200)
    parakeratosis=models.CharField(max_length=200)
    elongation=models.CharField(max_length=200)
    thinning=models.CharField(max_length=200)
    spongiform=models.CharField(max_length=200)
    munro=models.CharField(max_length=200)
    disappearance=models.CharField(max_length=200)
    vacuolisation=models.CharField(max_length=200)
    spongiosis=models.CharField(max_length=200)
    age=models.CharField(max_length=200)
    result=models.CharField(max_length=200)
    dt = models.DateField(auto_now_add=True)
    tm = models.TimeField(auto_now_add=True)
    status = models.CharField(max_length=255)


class Appointment_details(models.Model):
    doctor_name=models.ForeignKey(doctor_details,on_delete=models.CASCADE,related_name="appointment_doctor")
    patient_name=models.ForeignKey(Patient_details,on_delete=models.CASCADE,related_name="appointment_patient")
    date=models.CharField(max_length=200)
    time=models.CharField(max_length=200)
    dt = models.DateField(auto_now_add=True)
    tm = models.TimeField(auto_now_add=True)
    status = models.CharField(max_length=255)
