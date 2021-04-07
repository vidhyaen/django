from django.shortcuts import render
from django.shortcuts import  redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import Sellerregister,UserCreationForm,Affiliateregister,Userform


def index(request):
    if request.method == 'POST':
         user= request.POST['user']
         password = request.POST['pass']
         res = auth.authenticate(username=user, password=password)
         if res is not None:
            auth.login(request, res)
            return redirect('home')         
         else:
            messages.info(request,'username/password is invalid')
            return redirect('index')

    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = Userform(request.POST)
        if form.is_valid():
            print('Form is valid')
            form.save()
            return redirect('index')
        else:
            return render(request, 'register.html',{'form': form})
    form = Userform()
    return render(request,'register.html',{'form':form})

def Affiliate(request):
    if request.method == 'POST':
        form = Affiliateregister(request.POST)
        if form.is_valid():
            print('Form is valid')
            form.save()
            return redirect('/')
        else:
            return render(request, 'affiliateregister.html',{'form': form})
    form =Affiliateregister()
    return render(request,'affiliateregister.html',{'form':form}) 


def Seller(request):
    if request.method == 'POST':
        form = Sellerregister(request.POST)
        if form.is_valid():
            print('Form is valid')
            form.save()
            return redirect('index')
        else:
            return render(request, 'sellerregister.html',{'form': form})
    
    form =Sellerregister()
    return render(request,'sellerregister.html',{'form':form})       

@login_required(login_url='home')
def logout(request):
    auth.logout(request)
    return redirect('home')



