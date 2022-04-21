from django.shortcuts import render

# Create your views here.

def signup(request):
    return render(request, 'signup.html')


def signin(request):
    return render(request, 'signin.html')


def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def faq(request):
    return render(request, 'faq.html')

def home(request):
    return render(request, 'index.html')