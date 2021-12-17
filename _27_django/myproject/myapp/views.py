from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# class based based view
# function based view

def index(request):
    return HttpResponse('Hello Ali')


def name(request):
    response = """<p> Hi Ali you are in name</p>"""
    return HttpResponse(response)


def game(request, guess):
    response = """<h1> Hi Ali you are in page number """ + guess + """</h1>"""
    return HttpResponse(response)


# first we need to create a view
# we need to create a route in urls.py
# need to add that route in proj urls.py

# urls --> views --> check data base if we need to store data or retrive
# send data to html --> that file is viewed

# from url we got dynamic --> urls.py --> view.py --> function --> we are accessing
# --> we will process an sen back to fe


def html_route(request):
    return render(request, 'myapp/index.html')


# path('ali/<int: number>
def html_route2(request, number):
    context = {'number': number}
    return render(request, 'myapp/main.html', context)


def html_route3(request):
    names = ['Ali', 'Hussain', 'Alian']
    numbers = [2]
    context = {'names': names, 'numbers': numbers}
    return render(request, 'myapp/number.html', context)
