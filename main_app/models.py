from enum import unique
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    is_therapist = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    creation_date = models.DateField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return f"User full name: {self.first_name} {self.last_name}."
    


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    desired_treatment = models.TextField(max_length=250)

    def __str__(self) -> str:
        return f"Patient {self.user.first_name}, who says: {self.desired_treatment}"

class Therapist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    therapy_license = models.CharField(max_length=50)
    treatment_specialty = models.CharField(max_length=100)