from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def display(request):
    return render(request,'second.html',{'name':'WPAB'})