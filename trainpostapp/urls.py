from django.urls import path
from django.shortcuts import render,redirect
from .views import index, signupfunc, loginfunc, dashboard, listfunc, logoutfunc, detailfunc, goodfunc, readfunc
# ファイル読み込み関連のモジュール
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('top/', index, name='top'),
    path('dashboard/', dashboard, name="dashboard"),
    path('signup/', signupfunc, name="signup"),
    path('login/', loginfunc, name="login"),
    path('logout/', logoutfunc, name="logout"),
    path('list/', listfunc, name='list'),
    path('detail/<int:pk>/', detailfunc, name='detail'),
    path('good/<int:pk>/', goodfunc, name='good'),
    path('read/<int:pk>/', readfunc, name="read"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
