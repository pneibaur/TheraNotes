from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("accounts/signup/", views.signup, name='signup'),
    path("accounts/signup/therapist/", views.therapist_signup, name='therapist_signup'),
    path("accounts/signup/patient/", views.patient_signup, name='patient_signup'),
]
