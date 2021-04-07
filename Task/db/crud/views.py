from django.shortcuts import render,redirect
from .models import Crud

# Create your views here.

def insert(request):
    return render(request,'insert.html')
def datainsert(request):
    name=request.POST['name']    
    email=request.POST['email']   
    number=request.POST['number']   
    address=request.POST['address']
    res=Crud(name=name,email=email,number=number,address=address)
    res.save()
    return render(request,'insert.html')
def display(request):
    res=Crud.objects.all()
    return render(request,'display.html',{'res':res})  
def delete(request,id):
    res=Crud.objects.get(id=id)    
    res.delete()
    return redirect('display') 