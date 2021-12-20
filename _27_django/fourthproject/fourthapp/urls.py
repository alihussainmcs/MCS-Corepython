from django.urls import path
from .views import *
urlpatterns = [
    path('', home),
    path('contact/<str:num>', contact),
    path('htmlpage/', html_index),
    path('html_contact/<int:number>', html_contact),
    path('list/',html_list),
    path('dict/',html_dict),
    path('cbv/',ClassBasedView.as_view()),
    path('cbv2/<str:num>', ClassTwo.as_view()),
    path('cbv3/<str:page>', ClassThree.as_view()),
    path('cbv4/<str:page>', ClassFour.as_view()),
]
