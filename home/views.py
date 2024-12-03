from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    return HttpRequest("Bem vindo.")
