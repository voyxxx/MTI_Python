from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse, HttpResponseNotFound
from random import randint

products = {
    1: {'name': 'молоко', 'price': 80},
    2: {'name': 'хлеб', 'price': 90},
    3: {'name': 'сметана', 'price': 70},
    4: {'name': 'конфеты', 'price': 150},
}

def index(req):
    return render(req, 'index.html')

def catalog(req):
    return render(req, 'catalog.html', {'products':  products})

def contacts(req):
    return render(req, 'contacts.html')

def product(req, id):
    if id in products:
        return render(req, 'product.html', {'product': products[id]})
    return HttpResponseNotFound('Такого товара нет')

# def index(req):
#     return HttpResponse('<h1>Hello world</h1>')

# def rand(req):
#     num = randint(0, 10)
#     return HttpResponse(f'<h1>Случайное число: {num}</h1>')

# def index_2(req):
#     return HttpResponse('Это главная страница')

# def catalog(req):
#     txt = ''
#     for id in products:
#         txt += f'<a href="./{id}">{products[id]["name"]}</a><br>'
#     return HttpResponse(txt)

# def contacts(req):
#     return HttpResponse('Это контакты')

# def product(req, id):
#     if id in products:
#         return HttpResponse(f'{products[id]["name"]} - {products[id]["price"]} руб.')
#     return redirect('/store/catalog/', permanent=True)
    

# def greeting(req, name):
#     return HttpResponse(f'Hello, {name}!')

# def file(req):
#     return FileResponse(open('D:\Мои документы\Рабочий стол\WPytн-КБ-21\lesson_3\Вебинар 4 Презентация (1).pptx.pdf', 'rb'), as_attachment=True)