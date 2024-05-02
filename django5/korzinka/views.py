from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Product

# Create your views here.


def get_info(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'product.html', context=context)


