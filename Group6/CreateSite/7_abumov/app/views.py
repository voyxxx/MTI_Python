from django.http import HttpResponse
from django.shortcuts import render

def index(request):
  return HttpResponse("Hello, world. You're at the app index.") 

def my_view(request):
    return render(request, 'products.html')

def my_view2(request):
    return render(request, 'index.html')
