from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import PatientSignupForm, CustomUserCreationForm, TherapistSignupForm
from .models import Patient, Therapist, User
from django.contrib.auth import get_user_model


def home(request):
    return render(request, 'home.html')


def signup(request):
    return render(request, 'registration/signup.html')


def patient_signup(request):
    error_message = ''
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        patient_form = PatientSignupForm(request.POST)
        if user_form.is_valid() and patient_form.is_valid():
            user = user_form.save()
            p = Patient.objects.create(
                user=user, desired_treatment=patient_form.instance.desired_treatment)
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
        {'user_form': user_form, 'patient_form': patient_form,
            'error_message': error_message}
    )


def therapist_signup(request):
    error_message = ''
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        therapist_form = TherapistSignupForm(request.POST)
        if user_form.is_valid() and therapist_form.is_valid():
            user = user_form.save()
            t = Therapist.objects.create(
                user=user,
                therapy_license=therapist_form.instance.therapy_license,
                treatment_specialty=therapist_form.instance.treatment_specialty,
            )
            t.save()
            return redirect('home')
        else:
            error_message = 'Invalid Signup - please try again.'
    else:
        user_form = CustomUserCreationForm()
        therapist_form = TherapistSignupForm()
    return render(
        request,
        'registration/therapist_signup.html',
        {'user_form': user_form, 'therapist_form': therapist_form,
            'error_message': error_message}
    )


def therapist_index(request):
    therapists = Therapist.objects.all()
    return render(request, 'profiles/therapist_index.html', {'therapists': therapists})

def therapist_detail(request, therapist_id):
    therapist = Therapist.objects.get(user_id=therapist_id)
    return render(request, 'profiles/therapist_detail.html', {'therapist': therapist})