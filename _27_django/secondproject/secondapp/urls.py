from django.urls import path
from .views import *
urlpatterns = [
    path('', second),
    path('<str:name>/', second_1)

]
