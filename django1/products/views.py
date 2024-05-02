from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Product, Category
# Create your views here.


def get_info(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'index.html', context=context)


def get_products(request, pk):
    products = Product.objects.filter(category=pk)
    context = {
        'products': products
    }
    return render(request, 'products.html', context=context)


def detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product
    }
    # print(1)
    return render(request, 'detail.html', context=context)
