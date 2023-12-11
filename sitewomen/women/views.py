from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


# Create your views here.


def index(request: HttpRequest):
    data = {"title": "О сайте",
            "menu": menu,
            "float": 28.75,
            'lst': [1, 2, "abc", True],
            'set': {1, 2, 3, 4, 5},
            "dict": {'key1': 'value1', 'key2': 'value2'},
            "obj": MyClass(10, 20),
            }
    return render(request, 'women/index.html', context=data)


def about(request: HttpRequest):
    data = {"title": "О сайте",
            "menu": menu,
            }
    return render(request, 'women/index.html', context=data)


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
