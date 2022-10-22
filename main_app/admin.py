from django.contrib import admin
from main_app.models import User, Patient, Therapist

# Register your models here.
admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Therapist)