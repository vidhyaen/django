from django.shortcuts import render

import datetime

# Create your views here.
def login(request):
    return render(request,'login.html')
def display(request):
    name=request.POST['user']
    x = datetime.datetime.now()
    return render(request,'display.html',{'name':name,'x':x})
