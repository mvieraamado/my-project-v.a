from django.shortcuts import render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from index.forms import CreateAUser, EditAUser
from django.contrib.auth.decorators import login_required #para funciones
# from django.contrib.auth.mixins import LoginRequiredMixin   -->  se utiliza para clases basadas en vistas

def home(request):
    return render(request, 'index/index.html', {})

@login_required
def photos(request):
    return render(request, 'index/photos.html', {})

def my_login(request):
    if request.method == 'POST':
        form_login= AuthenticationForm(request, data=request.POST)
        if form_login.is_valid():
            username = form_login.cleaned_data['username']
            password = form_login.cleaned_data['password']
            
            user = authenticate(username = username, password = password)
            
            if user is not None:
                login(request, user)
                return render(request, 'index/index.html', {})
            else:
                return render(request, 'index/login.html', {'form_login': form_login, 'mensaje': 'No se encuentra autenticado'})
                
        else :
            return render(request, 'index/login.html', {'form_login': form_login, 'mensaje': 'Datos incorrectos'})
    else: 
        form_login= AuthenticationForm()
        return render (request, 'index/login.html', {'form_login': form_login, 'mensaje': ''})

def user_register (request):
    if request.method == 'POST':
        form_register = CreateAUser(request.POST)

        if form_register.is_valid():
            username = form_register.cleaned_data['username']
            
            form_register.save()
            return render(request, 'index/index.html', {'mensaje': f'Se creo exitosamente {username}'})
        else:
            return render(request, 'index/register.html', {'form_register': form_register})
    
    form_register = CreateAUser()
    return render(request, 'index/register.html', {'form_register': form_register, 'mensaje': ''})

@login_required
def user_edit (request):
    if request.method == 'POST':
        form_edit = EditAUser(request.POST)
        
        if form_edit.is_valid():
            data = form_edit.cleaned_data
            
            loggued_in_user = request.user
            loggued_in_user.email = data.get('email')
            loggued_in_user.first_name = data.get('first_name', '')
            loggued_in_user.last_name = data.get('last_name', '')
            
            if data.get('password1') == data.get('password2') and len(data.get('password2')) > 8:
                loggued_in_user.set_password(data.get('password1'))
                
            loggued_in_user.save()
            return render(request, 'index/index.html', {})
        else:
            return render(request, 'index/edit_user.html', {'form_edit': form_edit})
    form_edit = EditAUser(
        initial={
            'username' : request.user.username,
            'first_name' : request.user.first_name,
            'last_name' : request.user.last_name,
            'email' : request.user.email
        }
    )
    return render(request, 'index/edit_user.html', {'form_edit': form_edit})

    