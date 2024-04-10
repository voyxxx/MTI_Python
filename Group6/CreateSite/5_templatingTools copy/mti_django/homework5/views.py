from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse


def index(request):
    data = {"my_list": ["Tom", "Sam", "Bob", "Mike"]}
    return TemplateResponse(request, "index.html", data)
