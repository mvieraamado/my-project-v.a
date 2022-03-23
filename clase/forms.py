from django import forms

class ClientForm(forms.Form):
    name= forms.CharField(max_length=20)
    lastName= forms.CharField(max_length=20)
    job= forms.CharField(max_length=40)
    email= forms.EmailField()
    
class ManicuristForm(forms.Form):
    manicurist= forms.CharField(label='Search manicurist', max_length=20)