from django.shortcuts import render

# Create your views here.
def searchManicurist(request):
    return render(request, 'clase/search_manicurist.html', {})