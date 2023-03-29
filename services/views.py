from django.shortcuts import render
from .models import Service

# Create your views here.

def services(requests):
    services = Service.objects.all()
    return render(requests, "services/services.html", {'services': services})
