from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import PatientSignupForm, CustomUserCreationForm
from .models import Patient, User
from django.contrib.auth import get_user_model

def home(request):
    return render(request, 'home.html')

def signup(request):
    return render(request, 'registration/signup.html')

def therapist_signup(request):
    return render (request, 'registration/therapist_signup.html')


def patient_signup(request):
    error_message = ''
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        patient_form = PatientSignupForm(request.POST)
        if user_form.is_valid() and patient_form.is_valid():
            print("here is user_form: ", user_form)
            print('here is patient form: ', patient_form)
            user = user_form.save()
            print('here is user: ', user)
            p = Patient.objects.create(user=user)
            print("here is patient.user NOW: ", p)
            p.save()
            return redirect('home')
        else: 
            error_message = 'Invalid Signup - please try again.'
    else:
        user_form = CustomUserCreationForm()
        patient_form = PatientSignupForm()
    return render(
        request, 
        'registration/patient_signup.html', 
        {'user_form': user_form, 'patient_form': patient_form, 'error_message': error_message}
        )