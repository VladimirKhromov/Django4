from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# Create your views here.

def index(request: HttpRequest):
    return HttpResponse('Страница приложения women')


def categories(request: HttpRequest):
    return HttpResponse('<h1> статьи по категориям </h1>')
