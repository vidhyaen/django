

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,'try.html',{'title':'Add 2 nos'});
def add(request):
    val=int(request.POST["num1"]);
    val1=int(request.POST["num2"]);
    res=val+val1;
    return render(request,'result.html',{'result':res})