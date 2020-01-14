from django.core.mail import send_mail
from django.shortcuts import redirect

# Create your views here.
def send_login_email(request):
    return redirect('/')
