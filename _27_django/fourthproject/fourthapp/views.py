from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# FBV function based view
from django.views import View


def home(request):
    return HttpResponse('Welcome to home page.')


def contact(request, num):
    return HttpResponse('Welcome , your contact number is ' + num + '.')


def html_index(request):
    return render(request, 'fourthapp/index.html')


def html_contact(request, number):
    context = {'number': number}
    return render(request, 'fourthapp/contact.html', context)


def html_list(request):
    names = ['Ali', 'Alian', 'Alien']
    # num = [1, 2, 3]
    context = {'names': names}
    return render(request, 'fourthapp/details.html', context)


def html_dict(request):
    page_lists = ['first', 'second', 'third']
    page_nums = [1, 2, 3]
    context_1 = {'page_lists': page_lists, 'page_nums': page_nums}
    return render(request, 'fourthapp/dict.html', context_1)


# CBV  Class based views
# View TemplateView ListView APIView
class ClassBasedView(View):
    def get(self, request):
        return HttpResponse('Hi, Ali welcome to CBV ')

    def post(self, request):
        pass

    def put(self, request):
        pass


class ClassTwo(View):
    def get(self, request, num):
        context = {'num': num}
        return HttpResponse('Hi, your are in page ' + num)


# create a function create a class and its method
# create a template
# route url in urls.py
class ClassThree(View):
    def get(self, request, page):
        context = {'page': page}
        return render(request, 'fourthapp/block.html', context)


class ClassFour(View):
    def get(self, request, page):
        context = {'page': page}
        return render(request, 'fourthapp/block1.html', context)
