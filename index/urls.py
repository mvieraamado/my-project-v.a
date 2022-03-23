from django.urls import path 
from .views import home, photos

urlpatterns = [
    path('', home, name='home'),
    path('photos/', photos, name='photos')
]

