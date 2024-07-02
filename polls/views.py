from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Contact
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def about(request):
     return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
   if request.method == "POST":
       name = request.POST.get('name')
       email = request.POST.get('email')
       message = request.POST.get('message')  
       contact = Contact(name=name, email=email, message=message)
       contact.save()
       messages.success(request, 'Your message has been successfully submitted!')
   return render(request, 'contact.html')
