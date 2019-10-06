from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>ReAll-Home</h1>')

def userauth(request):
    return HttpResponse('<h1>Login/Register</h1>')