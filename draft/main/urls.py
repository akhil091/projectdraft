from django.contrib import admin
from django.urls import path
from django.views.generic.base import RedirectView
from main import views


urlpatterns = [
    path('',RedirectView.as_view(url="home")),
    path('home/', views.home),
    path('signup/', views.signup),
    path('signin/', views.signin),
    path('contact/', views.contact),
    path('about/', views.about),
    path('faq/', views.faq),
]