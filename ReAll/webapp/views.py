from django.shortcuts import render

def home(request):
    return render(request, 'webapp/home.html')

def userauth(request):
    return render(request, 'webapp/userauth.html')

