from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(doctor_details)
admin.site.register(Patient_details)
admin.site.register(Prediction_details_new)
admin.site.register(Appointment_details)
