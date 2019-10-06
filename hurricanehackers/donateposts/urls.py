from django.urls import path

from . import views

app_name = 'donateposts'
urlpatterns = [
    path('', views.index, name='index')
]