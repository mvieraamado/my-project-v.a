from django.shortcuts import render
from accounts.views import search_avatar

from clase.models import BlogPosts
# from accounts.views import search_avatar

def home(request):
    if request.user.is_authenticated:
        return render(request, 'index/home.html', {'search_avatar':search_avatar(request.user)})
    else:
        return render(request, 'index/home.html', {})

def about(request):
    if request.user.is_authenticated:
        return render(request, 'index/about.html', {'search_avatar':search_avatar(request.user)})
    else:
        return render(request, 'index/about.html', {})
    

    