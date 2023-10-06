from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('страница приложения')

def categories(request):
    return HttpResponse('<h1>статьи по категориям</h1>')
