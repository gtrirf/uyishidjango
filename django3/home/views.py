from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def print_hello(request):
    return HttpResponse('</h1>HELLO WORLD</h1><hr>')


def print_salom(request):
    return HttpResponse('salom')