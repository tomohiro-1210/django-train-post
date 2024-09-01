from django.http import HttpResponse
from django.shortcuts import render, redirect

def index(request):
   return HttpResponse('初期画面')