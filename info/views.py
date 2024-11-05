from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def index(request):
    homes=Home.objects.all()
    abouts=About.objects.all()
    services=Service.objects.all()
    clients=Client.objects.all()
    questions=Question2.objects.all()
    portfolio=PortfolioItem.objects.all()
    return render(request, 'index.html',{'homes':homes,'abouts':abouts,'services':services,'clients':clients,'questions':questions,'portfolio':portfolio}) 

def contact(request):
    if request.method == "GET":
        return redirect('info:index')
    elif request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject') 
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, subject=subject, message=message) 
        contact.save()
        return redirect('info:index') 

    