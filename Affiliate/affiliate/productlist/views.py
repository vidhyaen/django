
from django.shortcuts import render
from .forms import Uploadform
from .models import productTable
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
# Create your views here.
@login_required(login_url='index')
def upload(request):
    if request.method == 'POST':
        form = Uploadform(request.POST, request.FILES)
        if form.is_valid():
            print('uploaded')
            form.save()

    form = Uploadform()
    return render(request, 'upload.html', {'form': form})


def display(request):
    res = productTable.objects.all()
    return render(request, 'view.html', {'res': res})

def detail(request,id):
    res = productTable.objects.filter(id=id)
    return render(request,'detail.html',{'res':res})