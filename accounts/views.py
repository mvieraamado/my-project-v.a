from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import CreateAUser, EditFullUser
from django.contrib.auth.decorators import login_required
from .models import UserExtension


def my_login(request):
    
    if request.method == 'POST':
        form_login = AuthenticationForm(request, data=request.POST)
        
        if form_login.is_valid():
            username = form_login.cleaned_data['username']
            password = form_login.cleaned_data['password']
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return render(request, 'index/home.html', {})
            else:
                return render(request, 'accounts/login.html', {'form_login': form_login})
        else:
            return render(request, 'accounts/login.html', {'form_login': form_login})
    
    
    form_login = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form_login': form_login})

def register(request):
    
    if request.method == 'POST':
        form_register = CreateAUser(request.POST)
        
        if form_register.is_valid():
            username = form_register.cleaned_data['username']
            form_register.save()
            return render(request, 'index/home.html', {})
        else:
            return render(request, 'accounts/register.html', {'form_register': form_register})
            
    
    form_register = CreateAUser()
    return render(request, 'accounts/register.html', {'form_register': form_register})

@login_required
def edit_user(request):
    
    user_extension_logued, _ = UserExtension.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form_edit = EditFullUser(request.POST, request.FILES)
        
        if form_edit.is_valid():
            
            request.user.email = form_edit.cleaned_data['email']
            request.user.first_name = form_edit.cleaned_data['first_name']
            request.user.last_name = form_edit.cleaned_data['last_name']
            request.user.email = form_edit.cleaned_data['email']
            user_extension_logued.avatar = form_edit.cleaned_data['avatar']
            user_extension_logued.link = form_edit.cleaned_data['link']
            user_extension_logued.more_description = form_edit.cleaned_data['more_description']
            
            if form_edit.cleaned_data['password1'] != '' and form_edit.cleaned_data['password1'] == form_edit.cleaned_data['password2']:
                request.user.set_password(form_edit.cleaned_data['password1'])
            
            request.user.save()
            user_extension_logued.save()
            
            return render(request, 'index/home.html', {'search_avatar':search_avatar(request.user)})
        else:
            return render(request, 'accounts/edit_user.html', {'form_edit': form_edit, 'search_avatar':search_avatar(request.user)})
            
    
    form_edit = EditFullUser(
        initial={
            'email': request.user.email,
            'password1': '',
            'password2': '',
            'first_name': request.user.first_name,
            'last_name': request.user.last_name, 
            'avatar': user_extension_logued.avatar,
            'link': user_extension_logued.link,
            'more_description': user_extension_logued.more_description
        }
    )
    return render(request, 'accounts/edit_user.html', {'form_edit': form_edit, 'search_avatar':search_avatar(request.user)})


def search_avatar (user):
    return UserExtension.objects.filter(user=user)[0].avatar.url
    
    