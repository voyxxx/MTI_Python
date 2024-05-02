from django.http import HttpResponse
from django.shortcuts import render
from .forms import ClientForm, ProductForm
from .models import Product, Category

def form(req):
    return HttpResponse(f'Hello, form!')

def html_form(req):
    return render(req, 'html_form.html')

def response_form(req):
    if req.POST:
        return HttpResponse(f'Привет, {req.POST.get("name", "Гость")}. Твой телефон - {req.POST.get("phone")}')
    # print(req.GET['phone'])
    # print(req.GET.get('phone'))
    return HttpResponse(f'Привет, {req.GET.get("name", "Гость")}. Твой телефон - {req.GET.get("phone")}')

def django_form(req):
    # if req.POST:
    #     form = ClientForm(req.POST)
    #     if form.is_valid():
    #         return HttpResponse(f'Привет, {form.cleaned_data["name"]}. Твой телефон - {form.cleaned_data["phone"]}')
    form = ClientForm()
    return render(req, 'django_form.html', {'form': form})

def model_form(req):
    if req.POST:
        form = ProductForm(req.POST)
        if form.is_valid():
            form.save()
    form = ProductForm()
    return render(req, 'model_form.html', {'form': form})
