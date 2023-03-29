from django.shortcuts import render, HttpResponse

# Create your views here.

'''
Inicio home/
Historia about/
Servicios services/
Visítanos store/
Contacto contact/
Blog blog/
Sample sample/
'''


def home(requests):
    return render(requests, "core/home.html")


def about(requests):
    return render(requests, "core/about.html")



def store(requests):
    return render(requests, "core/store.html")


def contact(requests):
    return render(requests, "core/contact.html")


def blog(requests):
    return render(requests, "core/blog.html")


def sample(requests):
    return render(requests, "core/sample.html")
