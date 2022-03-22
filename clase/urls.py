from django.urls import path
from .views import searchManicurist

urlpatterns = [
    path('search_manicurist/', searchManicurist, name='search_manicurist')
]
