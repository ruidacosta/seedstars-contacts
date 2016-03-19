from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.db import IntegrityError

import re

from .models import Person

# Create your views here.
def index(request):
    return render(request,'welcome.html',{'message' :'Hello World!! You''re at contacts index'})
    
def list(request):
    list_contacts = Person.objects.all()
    context = { 'contact_list': list_contacts }
    return render(request,'list.html',context)
    
def add(request):
    return render(request,'add.html',{})
    
def insert(request):
    if request.POST['name'] == '' or request.POST['email'] == '':
        return render(request, 'add.html',{'error_message':'Empty fields not supported.'})
    
    if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", request.POST['email']):
        return render(request, 'add.html', {'error_message':'Please enter a valid email.'})
    
    try:
        person = Person(name=request.POST['name'],email=request.POST['email'])
        person.save(force_insert=True)
    except IntegrityError:
        return render(request, 'add.html', {'error_message':'This contact already exists.'})
    except:
        return render(request, 'add.html', {'error_message' : 'Failed to create contact.'})
    
    return redirect(reverse('List'))
