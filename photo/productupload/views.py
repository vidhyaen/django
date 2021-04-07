
from django.shortcuts import render
from .forms import Uploadform
from .models import productImage
from django.core.files.storage import FileSystemStorage
# Create your views here.

def upload(request):
    if request.method == 'POST':
        form = Uploadform(request.POST, request.FILES)
        if form.is_valid():
            print('uploaded')
            form.save()

    form = Uploadform()
    return render(request, 'upload.html', {'form': form})


def productdisplay(request):
    res = productImage.objects.all()
    return render(request, 'view.html', {'res': res})
