from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import ModelForm,Userform
# Create your views here.
def show(request):
    if request.method == 'POST':
        form = ModelForm(request.POST)
        if form.is_valid():
            print('Form is valid')
            form.save()
            return redirect('show')
        else:
            return render(request, 'show.html', {'form': form})
    
    form = ModelForm()
    return render(request, 'show.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = Userform(request.POST)
        if form.is_valid():
            print('Form is valid')
            form.save()
            return redirect('register')
        else:
            return render(request, 'register.html', {'form': form})

    form = Userform()
    return render(request,'register.html',{'form':form})