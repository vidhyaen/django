from django.shortcuts import render,redirect
from .models import TestSamples
# Create your views here.


def insert(request):
    return render(request, 'insert.html')

def datainsert(request):
    name = request.POST['name']
    address = request.POST['address']
    number = request.POST['mob']
    email = request.POST['email']
    res = TestSamples(name=name,address=address,number=number,email=email)
    res.save()
    return render(request,'insert.html')

def display(request):
     res = TestSamples.objects.all()
     return render(request,'display.html',{'res':res})

def update(request,id):
    res = TestSamples.objects.get(id=id)
    return render(request,'update.html',{'res':res})

def dataupdate(request,id):
    res = TestSamples.objects.get(id=id)
    res.name = request.POST['name']
    res.address = request.POST['address']
    res.number = request.POST['mob']
    res.email = request.POST['email']
    res.save()
    return redirect('display')

def delete(request,id):
    res = TestSamples.objects.get(id=id)
    res.delete()
    return redirect('display')