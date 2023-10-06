from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='contact-us'),
    path('register/', register, name='register'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
]
