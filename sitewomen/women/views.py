from django.http import HttpRequest, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
]


# Create your views here.


def index(request: HttpRequest):
    data = {"title": "главная страница",
            "menu": menu,
            "posts": data_db,
            }
    return render(request, 'women/index.html', context=data)


def about(request: HttpRequest):
    data = {"title": "О сайте",
            "menu": menu,
            }
    return render(request, 'women/index.html', context=data)


def show_post(request: HttpRequest, post_id):
    return HttpResponse(f"Отображение статьи с Id = {post_id}")


def addpage(request: HttpRequest):
    return HttpResponse("Добавление статьи")


def contact(request: HttpRequest):
    return HttpResponse("Обратная связь")


def login(request: HttpRequest):
    return HttpResponse("Авторизация")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
