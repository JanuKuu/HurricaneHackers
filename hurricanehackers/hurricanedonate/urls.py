from django.urls import path

from . import views

app_name = 'need'
urlpatterns = [
    path('', views.index, name='index')
]