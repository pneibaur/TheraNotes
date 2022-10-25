from enum import auto
from operator import mod
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    is_therapist = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    creation_date = models.DateField(auto_now_add=True)
    interests = models.TextField(max_length=250, default='')
    bio = models.TextField(max_length=250, default='')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self) -> str:
        return f"User {self.first_name} {self.last_name}"


class Patient(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    desired_treatment = models.TextField(
        max_length=250, default="")
    road_map = models.TextField(max_length=250, default='None set')

    def get_absolute_url(self):
        return reverse("patient_detail", kwargs={"patient_id": self.user_id})

    def __str__(self) -> str:
        return f"Patient {self.user}"


class Tx_Session(models.Model):
    creation_date = models.DateField(auto_now_add=True)
    session_chart = models.TextField(max_length=250, default='')
    chart_patient_sees = models.TextField(max_length=250, default='')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    def __str__(self):
        return f"Tx Session for patient {self.patient.user.first_name}: {self.session_chart[:50]} "


class Therapist(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    therapy_license = models.CharField(max_length=50)
    treatment_specialty = models.CharField(max_length=100)
    patient = models.ManyToManyField(Patient)
    session = models.ManyToManyField(Tx_Session)

    def __str__(self) -> str:
        return f"Therapist {self.user}, {self.therapy_license}"

class Session_Note(models.Model):
    creation_date = models.DateField(auto_now_add=True)
    note = models.TextField(max_length=250, default="")
    session = models.ForeignKey(Tx_Session, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"session note from {self.user.first_name}"