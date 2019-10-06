from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='reall-home'),
    path('userauth', views.userauth, name='user-authentication')
]
