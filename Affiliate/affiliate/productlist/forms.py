from .models import productTable
from django import forms

PCHOICES =( 
    ("silkcotton saree", "skincotton"), 
    ("linen sarees", "linen"), 
    ("chudimaterial", "chudi"), 
    ("jewells", "chain and earing"), 

) 
class Uploadform(forms.ModelForm):
    #category=forms.MultipleChoiceField(choices = PCHOICES)
    category = forms.CharField(widget=forms.Select(choices=PCHOICES))
    desc=forms.CharField(widget=forms.Textarea)
    class Meta:
        model = productTable
        fields = '__all__'

