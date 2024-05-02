from django.http import HttpResponse
from django.shortcuts import redirect, render
from app.forms import StudentForm, ProductPostForm


def add_page(request):
    if request.method == 'POST':
        form = ProductPostForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                form.add_error(None, "Ошибка в заполнении формы")
    person = ProductPostForm()
    return render(request, 'add.html', {'form': person})


def index(request):
  student = StudentForm()
  return render(request, 'index.html', {'form': student})


def my_form(request):
    return render(request, 'my_form.html')

# def index(request):
#   return HttpResponse("Hello, world. You're at the app index.") 

def my_view(request):
    return render(request, 'products.html')

def my_view2(request):
    return render(request, 'index.html')
