from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import TestForms



class ModelForm(forms.ModelForm):
    pass1 = forms.CharField(widget=forms.PasswordInput())
    pass2 = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = TestForms
        fields = ['username','pass1','pass2','email']

    def clean_pass2(self):
        pass1 = self.cleaned_data['pass1']
        pass2 = self.cleaned_data['pass2']
        if pass1 != pass2:
            raise forms.ValidationError('Mismatch Password')


class Userform(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']

    def save(self,commit=True):
        res = super(Userform,self).save(commit=False)
        res.first_name = self.cleaned_data['first_name']
        res.last_name = self.cleaned_data['last_name']
        res.email = self.cleaned_data['email']
        if commit:
            res.save()