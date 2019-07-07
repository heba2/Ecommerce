from django.shortcuts import render, redirect
from accounts.models import  User
from .models import Cart
from products.models import Product
from django.http import HttpResponse
# Create your views here.


def showCartPage(request, userName):
    user = User.objects.get(username=userName)
    carts = Cart.objects.filter(user=user)
    x = 0
    totalPrice = 0
    while (x < len(carts)):
        totalPrice = float(totalPrice) + float(carts[x].total)
        x += 1

    return render(request, 'cart.html', {'carts': carts, 'totalPrice': totalPrice})


def add_to_cart(request, name):
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
            obj = Cart(user=user, product=product, quantity=quantity, total=total)
            obj.save()
            carts = Cart.objects.filter(user=user)
            x = 0
            totalPrice = 0
            while x < len(carts):
                totalPrice = float(totalPrice) + float(carts[x].total)
                x += 1
            return render(request, 'cart.html', {'carts': carts, 'totalPrice': totalPrice})
        except Exception as e:
            return HttpResponse(e)
    else:
        return render(request, 'product-detail.html', {'data': singlePro})


def deleteCart(request, pk, userName):
    cart = Cart.objects.get(pk=pk)
    cart.delete()
    user = User.objects.get(username=userName)
    carts = Cart.objects.filter(user=user)
    x = 0
    totalPrice = 0
    while (x < len(carts)):
        totalPrice = float(totalPrice) + float(carts[x].total)
        x += 1

    return render(request, 'cart.html', {'carts': carts, 'totalPrice': totalPrice})



