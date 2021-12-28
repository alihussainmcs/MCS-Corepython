from django.shortcuts import render
import datetime


# Create your views here.


def wish(request):
    return render(request, 'testApp/wish.html')


def wishh(request):
    date = datetime.datetime.now()
    context = {'current_date': date}

    return render(request, 'testApp/wishh.html', context)


def temp_view(request):
    dt = datetime.datetime.now()
    e_name = 'Ali'
    e_id = 44
    e_mail = 'alihussain5499@gmail.com'
    context = {'now_date': dt, 'name': e_name, 'id': e_id, 'mail': e_mail}
    return render(request, 'testApp/result.html', context)


def wishhh(request):
    date = datetime.datetime.now()
    msg = 'Hello Guest !!!! Very Very Good '
    h = int(date.strftime('%H'))
    if h < 12:
        msg += 'Morning!!!'
    elif h < 16:
        msg += 'AfterNoon!!!'
    elif h < 21:
        msg += 'Evening!!!'
    else:
        msg = 'Hello Guest !!!! Very Very Good Night!!!'

    my_dict = {'insert_date': date, 'insert_msg': msg}
    return render(request, 'testApp/wishhh.html', context=my_dict)


def wishhhh(request):
    date = datetime.datetime.now()
    msg = None
    h = int(date.strftime('%H'))
    if h < 12:
        msg = 'Hello Guest !!!! Very Very Good Morning!!!'
    elif h < 16:
        msg = 'Hello Guest !!!! Very Very Good AfterNoon!!!'
    elif h < 21:
        msg = 'Hello Guest !!!! Very Very Good Evening!!!'
    else:
        msg = 'Hello Guest !!!! Very Very Good Night!!!'

    my_dict = {'insert_date': date, 'insert_msg': msg}

    return render(request, 'testApp/wishhhh.html', context=my_dict)


def moviesInfo(request):
    my_dict = {'head_msg': 'Movies Information',
               'sub_msg1': 'Angelina Jolie DCMG is an American actress and filmmaker. The recipient of numerous '
                           'accolades, including an Academy Award and three Golden Globe Awards, she has been named '
                           'Hollywoods highest-paid actress multiple times.',
               'sub_msg2': 'Bahubali-3 is just planning',
               'sub_msg3': 'Salman Khan ready to marriage',
               'photo': 'static/img/116.jpg'}
    return render(request, 'testApp/news.html', context=my_dict)


def sportsInfo(request):
    my_dict = {'head_msg': 'Sports Information',
               'sub_msg1': 'Anushka Sharma Firing Like anything',
               'sub_msg2': 'Kohli updating in game anything can happend',
               'sub_msg3': 'Worst Performance by India-Sehwag',
               }
    return render(request, 'testApp/news.html', context=my_dict)


def politicsInfo(request):
    my_dict = {'head_msg': 'Politics Information',
               'sub_msg1': 'Achhe Din Aaa gaya',

               'sub_msg2': 'Rupee Value now 1$:70Rs',
               'sub_msg3': 'In India Single Paisa Black money No more',
               }
    return render(request, 'testApp/news.html', context=my_dict)


def index(request):
    return render(request, 'testApp/index.html')
