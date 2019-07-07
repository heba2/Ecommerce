from django.shortcuts import render
from .models import Product, Category
from django.http import HttpResponse, JsonResponse


# Create your views here.


def products(request):
    categories = Category.objects.all()
    data = Product.objects.all()
    return render(request, 'shop.html', {'data': data, 'categories': categories})

############################################################


def categoryFilter(request, name):
    categories = Category.objects.all()
    category = Category.objects.get(name=name)
    data = Product.objects.filter(category_name=category)
    try:
        check = data[0]
        return render(request, 'shop.html', {'data': data, 'categories': categories})
    except:
        return render(request, 'shop.html', {'categories': categories, 'filterMessage':'No Products in this category yet'})

############################################################


def single_product(request, name):
    data = ""
    try:
        data = Product.objects.get(product_name=name)
    except Product.DoesNotExist:
        print('product doesnt exist')
    return render(request, 'product-detail.html', {'data': data})


