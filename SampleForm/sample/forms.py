from django import forms

class Sampleform(forms.Form):
    name = forms.CharField(widget=forms.TextInput())