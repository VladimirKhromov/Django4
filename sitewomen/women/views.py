from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse


# Create your views here.

def index(request: HttpRequest):
    return render(request, 'women/index.html')


def about(request: HttpRequest):
    return render(request, 'women/about.html')



def categories(request: HttpRequest, cat_id):
    print(request.GET)
    return HttpResponse(f'<h1> статьи по категориям </h1><p> id:{cat_id}</p>')


def categories_by_slug(request, cat_slug):
    print(request.GET)
    return HttpResponse(f'<h1> статьи по категориям </h1><p> slug:{cat_slug}</p>')


def archive(request, year):
    if year > 2023:
        uri = reverse('cats', args=('music',))
        return HttpResponseRedirect(uri)
    return HttpResponse(f'<h1>Архив по годам </h1><p> year :{year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
