import os
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

# Controller
# Django views.py is the Controller in MVC pattern

def index(request):
    context = {
        'eshop_env': os.environ.get("ESHOP_ENV", None),
    }
    return render(request, 'eshop/index.html', context)
