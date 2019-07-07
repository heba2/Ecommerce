from django.http import HttpResponse
from django.shortcuts import render, redirect
from accounts.models import User
from products.models import Product
from .models import Review


def add_review(request):
    username = request.GET.get('reviewer')
    user = User.objects.get(username=username)
    product_name = request.GET.get('product_rated')
    product = Product.objects.get(product_name=product_name)
    rating = int(request.GET.get('rating'))
    comment = request.GET.get('message')

    try:
        rev = Review(user=user, product=product, rating=rating, comment=comment)
        rev.save()
    except Exception as e:
        return HttpResponse('Error Try again')

    return redirect('/products/' + product_name+'/')

