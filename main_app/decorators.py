from cmath import log
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

def therapist_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    """
    Decorator for views that checks if the logged in user is_therapist=True. redirects to login page.
    CREDIT for help with this code goes to: Vitor Freitas! Thanks for your detailed article!
    https://simpleisbetterthancomplex.com/tutorial/2018/01/18/how-to-implement-multiple-user-types-with-django.html
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_therapist,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator

def patient_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='login'):
    """
    Decorator for views to check if the logged in user is_patient=True. redirects to login. 
    Credit again to Vitor Freitas!
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_patient,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator