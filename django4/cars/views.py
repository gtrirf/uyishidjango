from django.shortcuts import render
from .models import Cars, Category

# Create your views here.

def get_info(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'index.html', context=context)


def get_cars(request, pk):
    cars = Cars.objects.filter(category=pk)
    context = {
        'cars': cars
    }
    return render(request, 'cars.html', context=context)


def detail(request, pk):
    car = Cars.objects.get(pk=pk)
    context = {
        'car': car
    }
    return render(request, 'detail.html', context=context)