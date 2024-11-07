import pickle

import numpy as np
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

from dermatology_prediction import settings
from .models import *


# Create your views here.
def index(request):
    return render(request, "index.html")


#
def about(request):
    return render(request, "about.html")


#
def base(request):
    return render(request, "base.html")


def admin_login(request):
    return render(request, "admin_login.html")


def admin_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        # request.session['uid']=un
        message = "invalid"
        if user is not None:
            login(request, user)
            return redirect('/admin_dashboard/')
        else:
            return render(request, 'admin_login.html', {'message': message})


def admin_dashboard(request):
    return render(request, "admin_dashboard.html")


def add_doctor(request):
    return render(request, "add_doctor.html")


def save_doctor(request):
    if request.method == "POST":
        name = request.POST.get("name")
        level = request.POST.get("level")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        obj = doctor_details()
        obj.name = name
        obj.level = level
        obj.email = email
        obj.username = username
        obj.password = password
        obj.save()
        message = 'Username:%s \n Password:%s' % (obj.username, obj.password)
        send_mail('Login Details for doctors',
                  message,
                  settings.EMAIL_HOST_USER,
                  [obj.email])
        return redirect("/admin_dashboard/")


def view_doctor(request):
    d = doctor_details.objects.all()
    return render(request, "view_doctor.html", {"d": d})


def edit_doctor(request, id):
    doc = doctor_details.objects.get(id=id)
    return render(request, 'edit_doctor.html', {'doc': doc})


def update_doctor(request, id):
    d = doctor_details.objects.get(id=id)
    if request.method == "POST":
        d.name = request.POST.get('name')
        d.level = request.POST.get("level")
        d.email = request.POST.get("email")
        d.username = request.POST.get("username")
        d.password = request.POST.get("password")
        d.save()
        return redirect('/view_doctor/')
    else:
        return HttpResponse("Invalid data type")


def delete_doctor(request, id):
    d = doctor_details.objects.get(id=id)
    d.delete()
    return redirect("/view_doctor/")


def add_patient(request):
    data = doctor_details.objects.all()
    return render(request, "add_patient.html", {"data": data})


def save_patient(request):
    if request.method == "POST":
        doctor_name = request.POST.get("doctor_name")
        patient_name = request.POST.get("patient_name")
        address = request.POST.get("address")
        email = request.POST.get("email")
        mobile = request.POST.get("mobile")
        username = request.POST.get("username")
        password = request.POST.get("password")
        obj = Patient_details()
        obj.doctor_name_id = doctor_name
        obj.patient_name = patient_name
        obj.address = address
        obj.email = email
        obj.username = username
        obj.password = password
        obj.mobile = mobile
        obj.save()
        message = 'Username:%s \n Password:%s' % (obj.username, obj.password)
        send_mail('Login Details for Patient',
                  message,
                  settings.EMAIL_HOST_USER,
                  [obj.email])
        return redirect("/admin_dashboard/")
    else:
        HttpResponse("invalid data")


def view_patient(request):
    data = Patient_details.objects.all()
    return render(request, "view_patient.html", {"data": data})


def edit_patient(request, id):
    data = Patient_details.objects.get(id=id)
    return render(request, "edit_patient.html", {"data": data})


def update_patient(request, id):
    data = Patient_details.objects.get(id=id)
    if request.method == "POST":
        data.patient_name = request.POST.get("patient_name")
        data.address = request.POST.get("address")
        data.email = request.POST.get("email")
        data.mobile = request.POST.get("mobile")
        data.username = request.POST.get("username")
        data.password = request.POST.get("password")
        data.save()
        return redirect("/view_patient/")
    else:
        return HttpResponse("invalid data")


def delete_patient(request, id):
    data = Patient_details.objects.get(id=id)
    data.delete()
    return redirect("/view_patient/")


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#


def doctor_login(request):
    return render(request, "doctor_login.html")


def doctor_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if (doctor_details.objects.filter(username=username, password=password).exists()):
            loginobj = doctor_details.objects.get(username=username, password=password)
            request.session['d_id'] = loginobj.id

            return redirect('/doctor_dashboard/')
        else:
            message = "invalid"
            return render(request, 'doctor_login.html', {'message': message})


def doctor_dashboard(request):
    return render(request, "doctor_dashboard.html")


def view_my_patient(request):
    d_id = request.session['d_id']
    print(d_id, "iddddddddddd")
    data = Patient_details.objects.filter(doctor_name=d_id)
    return render(request, "view_my_patient.html", {"data": data})


def prediction(request):
    return render(request, "prediction.html")


def prediction1(request, id):
    data = Patient_details.objects.get(id=id)
    return render(request, "prediction1.html", {"data": data})


def save_prediction(request, id):
    model = pickle.load(open('derm.pkl', 'rb'))
    if request.method == "POST":
        patient_name = request.POST['fullname']
        erythema = request.POST['erythema']
        saw_tooth = request.POST['saw-tooth']
        melanin = request.POST['melanin']
        scaling = request.POST['scaling']
        itching = request.POST['itching']
        parakeratosis = request.POST['parakeratosis']
        elongation = request.POST['elongation']
        thinning = request.POST['thinning']
        spongiform = request.POST['spongiform']
        munro = request.POST['munro']
        disappearance = request.POST['disappearance']
        vacuolisation = request.POST['vacuolisation']
        spongiosis = request.POST['spongiosis']
        age = request.POST['age']

        arr = np.array([[erythema, saw_tooth, scaling, itching, parakeratosis, elongation, thinning, spongiform,
                         munro, disappearance, vacuolisation, spongiosis, age, melanin]])
        pred = model.predict(arr)
        d_id = request.session['d_id']
        obj = Prediction_details_new()
        obj.doctor_name_id = d_id
        obj.patient_name_id = id
        obj.erythema = erythema
        obj.saw_tooth = saw_tooth
        obj.scaling = scaling
        obj.itching = itching
        obj.melanin = melanin
        obj.parakeratosis = parakeratosis
        obj.elongation = elongation
        obj.thinning = thinning
        obj.spongiform = spongiform
        obj.munro = munro
        obj.disappearance = disappearance
        obj.vacuolisation = vacuolisation
        obj.spongiosis = spongiosis
        obj.age = age
        obj.save()
        if pred == [1]:
            obj.result = "Psoriasis"
            obj.save()
            status=0
            return render(request, 'result.html', {"status": status})
        elif pred == [2]:
            obj.result = " Aseboreic Dermatitis"
            obj.save()
            status = 1
            return render(request, 'result.html', {"status": status})
        elif pred == [3]:
            obj.result = "Lichen Planus"
            obj.save()
            status = 2
            return render(request, 'result.html', {"status": status})
        elif pred == [4]:
            obj.result = "Pityriasis rosea"
            obj.save()
            status = 3
            return render(request, 'result.html', {"status": status})
        elif pred == [5]:
            obj.result = "Cronic dermatitis"
            obj.save()
            status = 4
            return render(request, 'result.html', {"status": status})
        else:
            obj.result = "Pityriasis rubra pilaris"
            obj.save()
            status = 5
            return render(request, 'result.html', {"status": status})



def result(request):
    return render(request, "result.html")


def view_all_predictions(request):
    d_id = request.session["d_id"]
    data = Prediction_details_new.objects.filter(doctor_name=d_id)
    print(data)
    return render(request, "view_all_predictions.html", {"data": data})


##########################################################################################################


def user_login(request):
    return render(request,"user_login.html")


def user_login_view(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        if(Patient_details.objects.filter(username=username,password=password).exists()):
            loginobj = Patient_details.objects.get(username=username, password=password)
            request.session['u_id'] = loginobj.id
            return render(request,"user_dashboard.html")
        else:
            message="Invalid username or Password"
            return render(request,"user_login.html",{"message":message})
    else:
        return HttpResponse("invalid")


def user_dashboard(request):
    return render(request,"user_dashboard.html")


def my_profile(request):
    u_id=request.session['u_id']
    prf=Patient_details.objects.get(id=u_id)
    return render(request,"my_profile.html",{"prf":prf})


def change_profile(request):
    u_id=request.session['u_id']
    change_prf=Patient_details.objects.get(id=u_id)
    return render(request, "change_profile.html", {"change_prf": change_prf})


def update_profile(request):
    u_id=request.session['u_id']
    data=Patient_details.objects.get(id=u_id)
    data.patient_name=request.POST.get("patient_name")

    data.email = request.POST.get("email")
    data.mobile = request.POST.get("mobile")
    data.address = request.POST.get("address")
    data.username = request.POST.get("username")
    data.password=request.POST.get("password")
    data.save()
    return redirect("/my_profile/")



def my_result(request):
    u_id=request.session['u_id']
    d=Patient_details.objects.get(id=u_id)


    data=Prediction_details_new.objects.filter(patient_name=d)

    return render(request, "my_result.html",{"data":data})


def view_admin_prediction(request):
    data=Prediction_details_new.objects.all()
    return render(request,"view_admin_prediction.html",{"data":data})


def take_appointment(request):
    u_id=request.session['u_id']
    d=Patient_details.objects.get(id=u_id)
    return render(request,"take_appointment.html",{"d":d})


def save_appointment(request):
    u_id=request.session['u_id']
    d=Patient_details.objects.get(id=u_id)
    doctor_name=request.POST.get("doctor_name")
    doc=doctor_details.objects.get(name=doctor_name)
    if request.method=="POST":
        data=Appointment_details()
        data.doctor_name_id=doc.id
        data.patient_name_id=d.id
        data.status = "False"
        date = request.POST.get("date")
        time = request.POST.get("time")
        if(Appointment_details.objects.filter(date=date).exists()):
            return HttpResponse("Dates is not available")
        elif(Appointment_details.objects.filter(time=time).exists()):
            return HttpResponse("Time is not available")
        else:
            data.date=date
            data.time=time
            data.save()
            return redirect("/take_appointment/")

def save_confirmation(request,id):
    data=Appointment_details.objects.get(id=id)
    data.status="True"
    data.save()
    return redirect("/pending_appointment/")

def pending_appointment(request):
    data=Appointment_details.objects.filter(status="False")
    return render(request,"pending_appointment.html",{"data":data})



def confirm_appointment(request):
    data=Appointment_details.objects.filter(status="True")
    return render(request, "confirm_appointment.html", {"data": data})

def view_appointments(request):
    u_id=request.session['u_id']
    data=Appointment_details.objects.filter(patient_name=u_id)
    return render(request,"view_appointments.html",{"data":data})