from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):

    send_mail('Hola Omar', 'Este es un msm autogenerado', 
    'oromero@unsa.edu.pe', 
    ['oromero@unsa.edu.pe'], 
    fail_silently=False)
    return render(request, 'index.html')