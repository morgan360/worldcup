# films/urls.py
from django.urls import path
from .views import Main, UserInfo

app_name = 'films'
urlpatterns = [
    path('', Main.as_view(), name='main'),
    path('user_info/', UserInfo.as_view(), name='user'),
]