from django.http import HttpResponse
from django.shortcuts import render, redirect
from accounts.models import User
from .models import Contact


def contactPage(request):
    return render(request, 'contact.html')


def contact(request, userName):
    content = request.GET.get('content')
    subject = request.GET.get('subject')
    email = request.GET.get('contact_email')
    admin = User.objects.get(username='heba')
    sender = User.objects.get(username=userName)
    contact = Contact(sender=sender, contact_email=email, subject=subject, content=content, admin=admin)
    contact.save()
    return redirect('index')


def showMessages(request):
    messages = Contact.objects.all().order_by('date').reverse()
    return render(request, 'messages.html', {'messages': messages})
