from django.contrib import admin
from main_app.models import User, Patient, Therapist, Tx_Session, Session_Note

# Register your models here.
admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Therapist)
admin.site.register(Tx_Session)
admin.site.register(Session_Note)