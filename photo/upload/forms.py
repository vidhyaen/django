from .models import File_Tabel
from django import forms


class File_Form(forms.ModelForm):
    class Meta:
        model = File_Tabel
        fields = '__all__'