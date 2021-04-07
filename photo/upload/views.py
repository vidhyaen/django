from django.shortcuts import render
from .forms import File_Form
from .models import File_Tabel
from django.core.files.storage import FileSystemStorage
# Create your views here.


def upload(request):
    if request.method == 'POST':
        form = File_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()

    form = File_Form()
    return render(request, 'upload.html', {'form': form})


def display(request):
    res = File_Tabel.objects.all()
    return render(request, 'view.html', {'res': res})
