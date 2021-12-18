from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse('Hello, Welcome to third web page.')


def home(request):
    return HttpResponse('Welcome to home page .')


def register(request):
    return HttpResponse('Welcome to registration page ')


def contact(request):
    return HttpResponse('Welcome to contact page')


def about(request):
    return HttpResponse('Welcome to about page ')


def service(request):
    return HttpResponse('Welcome to service page ')
