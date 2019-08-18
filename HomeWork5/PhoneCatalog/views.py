from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, redirect

from .models import Clients

# Create your views here.

# главная страница со списком отсортированных Name
def index(request):
    message = None
    if "message" in request.GET:
        message = request.GET["message"]
    # создание HTML-страницы по шаблону index.html
    # с заданными параметрами alpha_Clients  м message
    return render(
        request,
        "index.html",
        {
            "alpha_Clients":
                Clients.objects.order_by('Name'),
            "message": message
        }

    )