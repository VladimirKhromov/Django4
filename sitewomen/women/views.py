from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound

# Create your views here.

def index(request: HttpRequest):
    return HttpResponse('Страница приложения women')


def categories(request: HttpRequest, cat_id):
    print(request.GET)
    return HttpResponse(f'<h1> статьи по категориям </h1><p> id:{cat_id}</p>')

def categories_by_slug(request, cat_slug):
    print(request.GET)
    return HttpResponse(f'<h1> статьи по категориям </h1><p> slug:{cat_slug}</p>')

def archive(request, year):
    return HttpResponse(f'<h1>Архив по годам </h1><p> year :{year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")