from django import forms
from django.contrib.auth.models import User
from .models import Sellerregister,Affiliateregister

from django.contrib.auth.forms import UserCreationForm

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

class Sellerregister(forms.ModelForm):
   
    class Meta:
        model = Sellerregister
        fields = '__all__'

   
class Affiliateregister(forms.ModelForm):
    
    class Meta:
        model =Affiliateregister
        fields ='__all__'

