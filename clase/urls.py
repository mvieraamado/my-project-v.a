from django.urls import path
from clase.views import search_manicurist, patient_form

urlpatterns = [
    path('search_manicurist/', search_manicurist, name='search_manicurist'),
    path('client/', patient_form, name = 'patient_form')
]
