from .models import User, Customer
from django.shortcuts import render, redirect
from .forms import UserForm, CustomerForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def checkout(request):
    return render(request, 'checkout.html')


def order_complete(request):
    return render(request, 'order-complete.html')


def add_wish(request):
    return render(request, 'add-wish.html')


@login_required
def log_out(request):
    logout(request)
    return render(request, 'logout.html')


def signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        customer_form = CustomerForm(request.POST)
        if user_form.is_valid() and customer_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            customer = customer_form.save(commit=False)
            customer.user = user
            customer.save()

            #########################################
            return redirect('/accounts/login/')
        else:
            print(user_form.errors, customer_form.errors)
    else:
        user_form = UserForm()
        customer_form = CustomerForm()

    #########################################
    return render(request, 'signup.html', {'user_form': user_form, 'customer_form': customer_form})


def log_in(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("Password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            print(user)
            return HttpResponse('Invalid Email or Password')
    else:
        return render(request, 'login.html')

