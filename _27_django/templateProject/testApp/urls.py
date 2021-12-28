from django.urls import path
from . import views

urlpatterns = [
    path('', views.wish),
    path('1/', views.wishh),
    path('2/', views.temp_view),
    path('3/', views.wishhh),
    path('4/', views.wishhhh),
    path('5/', views.moviesInfo),
    path('6/', views.sportsInfo),
    path('7/', views.politicsInfo),
    path('index/', views.index)

]