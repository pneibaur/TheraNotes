from pyexpat import model
from .models import Therapist, Patient, Session_Note
from django.forms import forms, ModelForm
from django.contrib.auth import forms, get_user_model


class CustomUserCreationForm(forms.UserCreationForm):
    class Meta:
        model= get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email', 'interests', 'bio', )

class PatientSignupForm(ModelForm):
    class Meta:
        model = Patient
        fields = ['desired_treatment',]

class TherapistSignupForm(ModelForm):
    class Meta:
        model = Therapist
        fields = ['therapy_license', 'treatment_specialty',]

class NoteForm(ModelForm):
    class Meta:
        model = Session_Note
        fields = ['note',]
