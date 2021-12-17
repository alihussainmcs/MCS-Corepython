from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index),
    path('name/', views.name),
    path('name/<str:guess>', views.game),
    path('html/', views.html_route),
    path('html/<int:number>', views.html_route2),
    path('html/loops/', views.html_route3),
]
