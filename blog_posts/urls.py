from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'), #(path, render function, namespace)
    path('about/', views.about, name='blog-about')
]
