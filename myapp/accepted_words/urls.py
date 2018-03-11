from django.urls import path, re_path
from . import views

urlpatterns = [
        re_path(r'^$', views.accept_words, name='accept_words'),
        re_path(r'^register$', views.registration, name='register')
        ]
