from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Ya resppnse")


def page1(request):
    return HttpResponse('1)Создать  2 функции, которые будут выдавать пользователю 2 любых фразы.')


def page2(request):
    return HttpResponse("""
        2)Создать вложенный путь к каждой из них:
        Пример:
        http://127.0.0.1:8000/pages/page1
        http://127.0.0.1:8000/pages/page2
    """)
