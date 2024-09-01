from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
# 認証関係のモジュール読み込み(Django標準搭載)
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# ログインの読み込み
from django.contrib.auth import login, authenticate, logout
# 自作物の読み込み
from .models import ListModel

# Errorの読み込み
from django.db import IntegrityError

# Create your views here.
def index(request):
   return HttpResponse('TOPページ')

# ログインのダッシュボード
@login_required
def dashboard(request):
   return HttpResponse('ログイン成功！')

# 新規登録ーページ
def signupfunc(request):
   template = 'signup.html'
   object_list = User.objects.all()
   if request.method == 'POST':
      username = request.POST['username']
      email = request.POST['email']
      password = request.POST['password']
      try:
         # Userモデルにデータを登録する
         user = User.objects.create_user(username, email, password)
         return redirect('login')
      except IntegrityError:
         error = "入力された名前・メールアドレスは既に使われております。"
         data = {'error': error}
         return render(request, template, data)
   else:
      print('リダイレクト')
   
      # 個別のデータを取り出す
      object = User.objects.get(username="hanshin")
      print(object.email)
      
   data = {}
   return render(request, template, data)

# ログイン
def loginfunc(request):
   template = 'login.html'
   if request.method == "POST":
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(request, username=username, password=password)
      if user is not None:
         login(request, user)
         return redirect('list')
      elif username == '' or password == '':
         error = "フォームが入力されていません"
         data = {'error':error}
         return render(request ,template ,data)
      else:
         return redirect('signup')
   
   data = {}
   return render(request, template ,data)

# ログアウト
@login_required
def logoutfunc(request):
   logout(request)
   return redirect('login')

# 投稿一覧
@login_required
def listfunc(request):
   template = 'list.html'
   object_list = ListModel.objects.all()
   
   data = {'object_list':object_list}
   return render(request ,template, data)

# 投稿詳細
@login_required
def detailfunc(request, pk):
   template = 'detail.html'
   # 個別のデータを読み込む
   object = get_object_or_404(ListModel, pk=pk)
   
   data = {'object':object}
   return render(request, template, data)

# いいね
def goodfunc(request, pk):
   
   object = ListModel.objects.get(pk=pk)
   object.good = object.good + 1
   object.save()
   return redirect('list')

# 既読
def readfunc(request, pk):
   object = ListModel.objects.get(pk=pk)
   username = request.user.get_username()
   if username in object.readuser:
      return redirect('list')
   else:
      object.read = object.read + 1
      object.readuser = object.readuser + ', ' + username
      object.save()
      return redirect('list')
      