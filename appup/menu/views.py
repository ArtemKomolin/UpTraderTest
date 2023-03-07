from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from .models import *


def index(request):
    menu = Albums.objects.all()
    songs = Songs.objects.all()
    context = {
        'menu': menu,
        'songs': songs,
        'title': 'Тестовое задание Menu от Комолина Артёма'
    }
    return render(request, 'menu/index.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
