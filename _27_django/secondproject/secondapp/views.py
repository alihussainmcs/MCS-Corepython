from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def second(request):
    return HttpResponse("<h10> Hi , this is my home page of django project </h10>")


def second_1(request, name):
    return HttpResponse('Hi ' + name + ' Welcome my friend welcome')
