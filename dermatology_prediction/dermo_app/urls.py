from django.urls import path

from dermo_app import views

urlpatterns = [
    path('', views.index),
    path('index/',views.index),
    path('about/',views.about),
    path('base/',views.base),
    path("admin_login/",views.admin_login),
    path("admin_login_view/",views.admin_login_view),
    path("admin_dashboard/",views.admin_dashboard),
    path("add_doctor/",views.add_doctor),
    path("save_doctor/",views.save_doctor),
    path("view_doctor/",views.view_doctor),
    path("edit_doctor/<id>/",views.edit_doctor),
    path("update_doctor/<id>",views.update_doctor),
    path("delete_doctor/<id>",views.delete_doctor),
    path("add_patient/",views.add_patient),
    path("save_patient/",views.save_patient),
    path("view_patient/",views.view_patient),
    path("edit_patient/<id>",views.edit_patient),
    path("update_patient/<id>",views.update_patient),
    path("view_admin_prediction/",views.view_admin_prediction),



    path("doctor_login/",views.doctor_login),
    path("doctor_login_view/",views.doctor_login_view),
    path("doctor_dashboard/",views.doctor_dashboard),
    path("view_my_patient/",views.view_my_patient),
    path("prediction/",views.prediction),
    path("prediction/<id>",views.prediction1),
    path("save_prediction/<id>",views.save_prediction),
    path("result/",views.result),
    path("view_all_predictions/",views.view_all_predictions),
    path("pending_appointment/",views.pending_appointment),
    path("confirm_appointment/",views.confirm_appointment),
    path("save_appointment/",views.save_appointment),
    path("save_confirmation/<id>",views.save_confirmation),
    path("view_appointments",views.view_appointments),




    path("user_login/",views.user_login),
    path("user_dashboard/",views.user_dashboard),
    path("user_login_view/",views.user_login_view),
    path("my_profile/",views.my_profile),
    path("change_profile/",views.change_profile),
    path("update_profile/",views.update_profile),
    path("my_result/",views.my_result),
    path('take_appointment/',views.take_appointment),



]