import random
from django.template.response import TemplateResponse


def index(request):
    return TemplateResponse(request,  "index.html")


def game(request):
    numbers, length = get_three_random_number()
    data = {
        "numbers": numbers,
        "len": length
    }
    return TemplateResponse(request, "game.html", data)


def get_three_random_number():
    arr = [random.randint(0, 3) for _ in range(3)]
    length = len(set(arr))
    return arr, length
