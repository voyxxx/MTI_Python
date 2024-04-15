from django.shortcuts import render
from django.http import FileResponse, HttpResponse

# Create your views here.

def index(request):
  return HttpResponse('workWithFiles index')

def picture(request):
    return FileResponse(open('workWithFiles/static/image/forest.jpg', 'rb'), as_attachment=True)