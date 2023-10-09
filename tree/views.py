from django.shortcuts import render
from django.http import HttpRequest


# Create your views here.
def menu(request: HttpRequest, link: str = ''):
    return render(request, 'menu.html')
