from django.shortcuts import render,redirect
from store.models import Product

from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail

from contact.models import contact

def home(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email = request.POST.get('email')
        recipient_list = ['shahlathasni3@gmail.com']
        send_mail( subject, message, email, recipient_list,name )


    
    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request,"home.html",context)

