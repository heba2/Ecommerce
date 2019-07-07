from django.shortcuts import render
from products.models import Product, Category


def search(request):
    categories = Category.objects.all()
    productName = request.GET.get('searchedProduct')
    try:
        product = Product.objects.filter(product_name=productName)
        return render(request, 'shop.html', {'data': product, 'categories': categories})
    except Exception as e:
        return render(request, 'shop.html', {'message': 'Not Found', 'categories': categories})


