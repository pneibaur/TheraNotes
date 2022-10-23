from django.shortcuts import render, redirect
from .forms import PatientSignupForm, CustomUserCreationForm, TherapistSignupForm
from .models import Patient, Therapist
from django.contrib.auth.decorators import login_required
# Credit to Vitor Frietas for the guide on making decorators. see decorators.py for URL
from .decorators import therapist_required, patient_required


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
            user = user_form.save(commit=False)
            user.is_patient = True
            user.save()
            p = Patient.objects.create(
                user=user, desired_treatment=patient_form.instance.desired_treatment)
            p.save()
            return redirect('patient_detail', patient_id=p.user_id)
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
            user = user_form.save(commit=False)
            user.is_therapist = True
            user.save()
            # set save to commit=False, then flip the boolean for is_therapist!
            t = Therapist.objects.create(
                user=user,
                therapy_license=therapist_form.instance.therapy_license,
                treatment_specialty=therapist_form.instance.treatment_specialty,
            )
            t.save()
            return redirect('therapist_detail', therapist_id=t.user_id)
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
    return render(request, 'profiles/profile_index.html', {'therapists': therapists})


def therapist_detail(request, therapist_id):
    therapist = Therapist.objects.get(user_id=therapist_id)
    return render(request, 'profiles/profile_detail.html', {'therapist': therapist})

@login_required
@therapist_required
def patient_index(request, therapist_id):
    therapist_patients = Therapist.objects.get(
        user_id=therapist_id).patient.all()
    unassigned_patients = Patient.objects.filter(therapist__isnull=True)
    return render(request, 'profiles/profile_index.html', {"therapist_id": therapist_id, 'therapist_patients': therapist_patients, 'unassigned_patients': unassigned_patients})

@login_required
def patient_detail(request, patient_id):
    patient = Patient.objects.get(user_id=patient_id)
    return render(request, 'profiles/profile_detail.html', {'patient': patient})

@login_required
@therapist_required
def patient_assign(request, therapist_id, patient_id):
    print("YOU ARE NOW IN ASSIGN_PATIENT")
    p = Patient.objects.get(user_id=patient_id)
    Therapist.objects.get(user_id=therapist_id).patient.add(p)
    return redirect('patient_index', therapist_id=therapist_id)

@login_required
@therapist_required
def patient_unassign(request, therapist_id, patient_id):
    p = Patient.objects.get(user_id=patient_id)
    Therapist.objects.get(user_id=therapist_id).patient.remove(p)
    return redirect('patient_index', therapist_id=therapist_id)

@login_required
def patient_home(request, patient_id):
    patient = Patient.objects.get(user_id=patient_id)
    therapists = patient.therapist_set.all()
    return render(request, "patient/patient_home.html", {"patient": patient, 'therapists': therapists})

