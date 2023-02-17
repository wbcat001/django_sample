from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path("",views.hello,name="hello")#空のテキストを指定
]