from .models import productImage
from django import forms

PCHOICES =( 
    ("1", "skincotton"), 
    ("2", "linen"), 
    ("3", "chudi"), 
    ("4", "chain and earing"), 

) 
class Uploadform(forms.ModelForm):
    category=forms.MultipleChoiceField(choices = PCHOICES)
    class Meta:
        model = productImage
        fields = '__all__'