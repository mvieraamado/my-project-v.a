from django import forms
from ckeditor.fields import RichTextFormField

class ClientForm(forms.Form):
    name= forms.CharField(max_length=20)
    lastName= forms.CharField(max_length=20)
    job= forms.CharField(max_length=40)
    email= forms.EmailField()
    
class ManicuristForm(forms.Form):
    manicurist= forms.CharField(label='Search manicurist', max_length=20)
    
class MyBlogPostsForm (forms.Form):
    title = forms.CharField(max_length=100)
    subtitle = forms.CharField(max_length=140)
    content = RichTextFormField(required=False)
    image = forms.ImageField(required=False)
    
class BlogPostSearch(forms.Form):
    nombre = forms.CharField(label='Search', max_length=50)
    