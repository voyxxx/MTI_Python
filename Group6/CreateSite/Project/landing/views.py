from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Product as ProductModel, Consumer as ConsumerModel
import re

phone_pattern = r'^\d{3}-\d{3}-\d{4}$'


def index(request):
    products = list(ProductModel.objects.all())
    return render(request, 'index.html', {'products': products})

def callback(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        comment = request.POST.get('comment')
        is_agree = request.POST.get('is_agree')
        print(f'name: {name}, phone: {phone}, comment: {comment}, is_agree: {is_agree}')
        if len(name)>2 and re.match(phone_pattern, phone) and is_agree == 'on':
            ConsumerModel.objects.create(name=name, phone=phone.replace('-', ''), comment=comment, is_agree=True)
        else:
            print('error')
            return HttpResponse(f'Имя должно быть более двух символов и телефон в формате xxx-xxx-xxxx и согласие на обработку персональных данных')
    return redirect('/')
            