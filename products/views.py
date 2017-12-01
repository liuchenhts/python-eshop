import os
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from .models import Product
from .forms import ProductForm

# Controller
# Django views.py is the Controller in MVC pattern

def index(request):
    return HttpResponseRedirect(reverse('products:list'))

def list(request):
    latest_production_list = Product.objects.order_by('-created_date')[:50]
    context = {
        'latest_production_list': latest_production_list,
        'eshop_env': os.environ.get("ESHOP_ENV", None),
    }
    return render(request, 'product/list.html', context)

def create(request):
    if request.method == 'GET':
        form = ProductForm()
    else:
        # A POST request: Handle Form Upload
        # Bind data from request.POST into a Form
        form = ProductForm(request.POST)
        # If data is valid, proceeds to create a new record and redirect the user
        if form.is_valid():
            product = form.save()
            return HttpResponseRedirect(reverse('products:read', kwargs={'pk': product.id}))

    context = {
        'form': form,
    }
    return render(request, 'product/create.html', context)


# This is the usage of normal controller action
# This way is more flexible than generic view for complex situations
def read(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
            'product': product,
    }
    return render(request, 'product/read.html', context)

# # This is the usage of generic
# class read(generic.DetailView):
#     model = Product
#     template_name = 'product/read.html'

def update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        form = ProductForm(instance=product)
    else:
        # A POST request: Handle Form submit
        # Create Form from instance in db, then merge post request data to update
        form = ProductForm(request.POST, instance=product)
        # If data is valid, proceeds to create a new record and redirect the user
        if form.is_valid():
            product = form.save()
            return HttpResponseRedirect(reverse('products:read', kwargs={'pk': product.id}))

    context = {
        'form': form,
        'product': product,
    }
    return render(request, 'product/update.html', context)

def delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return HttpResponseRedirect(reverse('products:list'))
