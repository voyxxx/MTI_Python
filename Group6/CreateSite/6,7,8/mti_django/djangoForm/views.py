from django.shortcuts import render
from django.template.response import TemplateResponse
from djangoForm.forms import Person
from djangoForm.models import Person as PersonModel

def index(request):
  if request.method == "POST":
      name = request.POST.get("firstname")
      age = request.POST.get("lastname")
      PersonModel.objects.update_or_create(firstname=name, lastname=age)
      
  person = Person()
  return render(request, 'index.html', {'form': person})


def data(request):
  data = PersonModel.objects.all()
  print(data)
  return TemplateResponse(request, 'data.html', {'data': data})

# person_data = PersonModel.objects.all()  # Получение данных из PersonModel
#     return render(request, 'data.html', {'person_data': person_data})
