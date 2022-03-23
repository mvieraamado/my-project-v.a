from http.client import HTTPResponse
from django.shortcuts import redirect, render
from clase.forms import ManicuristForm, ClientForm
from clase.models import Client_n, Manicurist

# Create your views here.
def manicurist_new(request):
    manicurist_new = Manicurist(name = 'Juan', lastName = 'villareal', email = 'juanv@gmail.com')
    manicurist_new.save()
    return HTTPResponse(f"Manicurist: {manicurist_new.lastName} {manicurist_new.name}")

def search_manicurist(request):
    search_for_manicurists = []
    dato = request.GET.get('manicurist', None)
    if dato is not None:
        search_for_manicurists = Manicurist.objects.filter(name__icontains = dato)
    
    my_form= ManicuristForm()
    return render(request, 'clase/search_manicurist.html', {'my_form': my_form, 'search_for_manicurists': search_for_manicurists, 'dato': dato})

def patient_form(request):
    if request.method == 'POST':
        form_client= ClientForm(request.POST)
        if form_client.is_valid():
            data= form_client.cleaned_data
            new_client= Client_n(name= data['name'], lastName = data['lastName'], job = data['job'], email = data['email'])
            new_client.save()
            return redirect(patient_form)
    else:
        form_client= ClientForm()
    return render(request, 'clase/patient_form.html', {'form_client': form_client})

    