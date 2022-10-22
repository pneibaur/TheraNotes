from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    # ACCOUNTS SIGNUP
    path("accounts/signup/", views.signup, name='signup'),
    path("accounts/signup/therapist/", views.therapist_signup, name='therapist_signup'),
    path("accounts/signup/patient/", views.patient_signup, name='patient_signup'),
    # THERAPISTS
    path("therapists/", views.therapist_index, name='therapist_index'),
    path("therapists/<int:therapist_id>", views.therapist_detail, name='therapist_detail'),
    # PATIENTS
    path("patients/<int:therapist_id>", views.patient_index, name='patient_index'),
    path("patients/<int:patient_id>", views.patient_detail, name='patient_detail'),
]
