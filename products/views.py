from django.http import HttpResponse
from django.shortcuts import render
from .models import Item


# Create your views here.
def index(request):
    items = Item.objects.all()
    return render(request, 'index.html',
                  {'products': items})


def new(request):
    return HttpResponse("New products")
