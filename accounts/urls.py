from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import my_login, register, edit_user

urlpatterns = [
    path('login/', my_login, name='login'),
    path('edit/', edit_user, name='edit_user'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name='index/home.html'), name='logout'),
]