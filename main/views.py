from django.shortcuts import render
from django.http import HttpResponse


def hello(req, pk):
    return HttpResponse(f'Тестовая страница: {pk}')


def main_page(req):
    return HttpResponse('Главная страница')