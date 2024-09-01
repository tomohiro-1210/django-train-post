from django.shortcuts import render, redirect
from django.http import HttpResponse
# Useモデルの読み込み(Django標準搭載)
from django.contrib.auth.models import User

# Create your views here.
def index(request):
   return HttpResponse('TOPページ')

# 新規登録ーページ
def signupfunc(request):
   template = 'signup.html'
   object_list = User.objects.all()
   if request.method == 'POST':
      username = request.POST['username']
      email = request.POST['email']
      password = request.POST['password']
      # Userモデルにデータを登録する
      user = User.objects.create_user(username, email, password)
   else:
      print('リダイレクト')
   
      # 個別のデータを取り出す
      object = User.objects.get(username="hanshin")
      print(object.email)
      
   data = {}
   return render(request, template, data)