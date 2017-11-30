from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Django views.py is the controller in MVC pattern

def index(request):
    latest_production_list = Product.objects.order_by('-created_date')[:5]
    output = ', '.join([p.name for p in latest_production_list])
    return HttpResponse("Hello, world. You're at the products index. {}".format(output))

def create(request):
    return HttpResponse("create product")

def read(request, id):
    response = "read product %s."
    return HttpResponse(response % id)

def update(request, id):
    return HttpResponse("update product %s." % id)

def delete(request, id):
    return HttpResponse("delte product %s." % id)
