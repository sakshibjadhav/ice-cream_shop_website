from django.shortcuts import render,HttpResponse
from datetime import datetime
from myapp.models import Orders
from myapp.models import Contacts
from django.contrib import messages
# Create your views here.
def menu(request):
    return render(request,'menu.html')

def order(request):
    if request.method=="POST":
        name = request.POST.get('name')
        address =request.POST.get('address')
        itype = request.POST.get('itype')
        flavour =request.POST.get('flavour')
        quantity =request.POST.get('quantity')
        order = Orders(name=name , address=address, itype=itype, flavor=flavour, quantity=quantity, date=datetime.today())
        order.save()
        messages.success(request, 'Thank you for placing order.')
    return render(request,'order.html')

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        contact=request.POST.get('contact')
        email=request.POST.get('email')
        feedback=request.POST.get('feedback')
        new_review=Contacts(name=name, contact=contact, email=email, feedback=feedback, date=datetime.today())
        new_review.save()
        messages.success(request, 'Thanks for giving the feedback.')
    return render(request,'contact.html')
