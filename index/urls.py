from django.urls import path 
from .views import home, photos, my_login, user_register, user_edit
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name='home'),
    path('photos/', photos, name='photos'),
    path('login/', my_login, name='login'),
    path('logout/', LogoutView.as_view(template_name='index/index.html'), name='logout'),
    path('register/', user_register, name='register'),
    path('edit/', user_edit, name='edit')
]

