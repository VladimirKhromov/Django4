from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse


# from django.template.loader import render_to_string

menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


# Create your views here.
def index(request):
    data = {'title': "Main pages",
            'menu': menu,
    }
    return render(request, 'women/index.html', context=data)


def about(request):
    data = {'title': "about"}
    return render(request, 'women/about.html', data)


def categories(request, cat_id):
    return HttpResponse(f'<h1>статьи по категориям</h1><p>id: {cat_id}')


def categories_by_slag(request, cat_slug):
    if request.POST:
        print(request.POST)
    return HttpResponse(f'<h1>статьи по категориям</h1><p>id: {cat_slug}')


def archive(request, year):
    if year > 2023:
        uri = reverse('cats', args=("music",))
        return redirect(uri)

    return HttpResponse(f'<h1>архив</h1><p>id: {year}')


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена<h1>")
