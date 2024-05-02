from django.shortcuts import render
from .forms import ClientForm

def index(req):
    error = ''
    if req.POST:
        form = ClientForm(req.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма заполнена некорректно'
    return render(req, 'index.html', {'form': ClientForm(), 'error': error})
