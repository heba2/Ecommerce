from django.shortcuts import render, redirect
from accounts.models import  User
from .models import Wish
from products.models import Product
from django.http import HttpResponse
# Create your views here.


def showWishPage(request, userName):
    user = User.objects.get(username=userName)
    wishs = Wish.objects.filter(user=user)
    x = 0
    totalPrice = 0
    while (x < len(wishs)):
        totalPrice = float(totalPrice) + float(wishs[x].total)
        x += 1

    return render(request, 'add-wish.html', {'wishs': wishs, 'totalPrice': totalPrice})


def add_to_wish(request, name):
    singlePro = Product.objects.get(product_name=name)
    if request.method == 'POST':
        userName = request.POST.get('userName')
        user = User.objects.get(username=userName)
        productName = request.POST.get('productName')
        product = Product.objects.get(product_name=productName)
        quantity = request.POST.get('quantity')
        price = request.POST.get('productPrice')
        total = float(quantity) * float(price)

        try:
            obj = Wish(user=user, product=product, quantity=quantity, total=total)
            obj.save()
            wishs = Wish.objects.filter(user=user)
            x = 0
            totalPrice = 0
            while x < len(wishs):
                totalPrice = float(totalPrice) + float(wishs[x].total)
                x += 1
            return render(request, 'add-wish.html', {'wishs': wishs, 'totalPrice': totalPrice})
        except Exception as e:
            return HttpResponse(e)
    else:
        return render(request, 'product-detail.html', {'data': singlePro})


def deleteWish(request, pk, userName):
    wish = Wish.objects.get(pk=pk)
    wish.delete()
    user = User.objects.get(username=userName)
    wishs = Wish.objects.filter(user=user)
    x = 0
    totalPrice = 0
    while (x < len(wishs)):
        totalPrice = float(totalPrice) + float(wishs[x].total)
        x += 1

    return render(request, 'add-wish.html', {'wishs': wishs, 'totalPrice': totalPrice})




