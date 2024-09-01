from django.urls import path
from django.shortcuts import render,redirect
from .views import index, signupfunc

urlpatterns = [
    path('top/', index, name='top'),
    path('signup/', signupfunc, name="signup"),
]
