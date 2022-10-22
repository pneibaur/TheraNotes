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
    interests = models.TextField(max_length=250, default='None added')
    bio = models.TextField(max_length=250, default='No bio added')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self) -> str:
        return f"User full name: {self.first_name} {self.last_name}"


class Patient(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    desired_treatment = models.TextField(
        max_length=250, default="Patient didn't specify...")
    road_map = models.TextField(max_length=250, default='No current road map')

    def get_absolute_url(self):
        return reverse("patient_detail", kwargs={"patient_id": self.user_id})
    

    def __str__(self) -> str:
        return f"Patient {self.user.first_name}, who wants: {self.desired_treatment}"


class Therapist(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    therapy_license = models.CharField(max_length=50)
    treatment_specialty = models.CharField(max_length=100)
    patient = models.ManyToManyField(Patient)

    def __str__(self) -> str:
        return f"Therapist {self.user}, with licence {self.therapy_license}, specializing in {self.treatment_specialty}"
