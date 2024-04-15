from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def my_view(request):
    return render(request, 'my_template.html')

def contacts(request):
    return render(request, 'contacts.html')

def about(request):
    return render(request, 'about_us.html')

def products(request):
    return render(request, 'products.html')