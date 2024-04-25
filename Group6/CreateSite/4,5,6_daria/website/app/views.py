from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, FileResponse, HttpResponseNotFound, JsonResponse
from random import randint, choice
from .models import Category, Product

def test(req):
  return render(req, 'test.html')

def show_json(req):
    data = {
        "info": {
        "name": "Vasya",
        "age": 65,
        "animals": [
            {"is_cat": True, "name": "Murka"},
            {"is_cat": False, "name": "Homa"}
        ],
        "children": None
      }
    }
    return JsonResponse(data)

def rand_product(req):
    data = choice(list(products.values()))
    data['url'] = 'http://127.0.0.1:8000/rand' + data['path']
    return JsonResponse(data)

def img_product(req, path_to_photo):
    return FileResponse(open('./app/static/image/' + path_to_photo, 'rb'))

products = {
    1: {'name': 'молоко', 'price': 80, 'path': 'milk.png'},
    2: {'name': 'хлеб', 'price': 90, 'path': 'bread.png'},
    3: {'name': 'сметана', 'price': 70, 'path': 'smetana.jpg'},
    4: {'name': 'конфеты', 'price': 150, 'path': 'sweets.jpg'},
}

def index(req):
    return render(req, 'index.html')

def catalog(req):
  print(Product.objects.all())
  return render(req, 'catalog.html', {'products':  Product.objects.all()})

def contacts(req):
    return render(req, 'contacts.html')

def product(request, product_name):
    products = Product.objects.all()
    for product in products:
        if product.link_name == product_name:
            return render(request, 'product.html', {'product': product})
    return HttpResponseNotFound('Такого товара нет')

# def product(req, product_name):
#     print(Product.objects.get(name=product_name))
#     print(Product.objects.all())
#     print(product_name in Product.objects.all())
#     # if product in Product.objects.all():
#     #     product = Product.objects.get(name=product)
#     #     print(product)
#     #     return render(req, 'product.html', {'product': product})
#     return HttpResponseNotFound('Такого товара нет')


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