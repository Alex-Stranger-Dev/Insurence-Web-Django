from django import forms

from .models import Persone, Phone


class CreatePersoneForm(forms.ModelForm):
    phones = forms.CharField(widget=forms.TextInput())
    name = forms.CharField(widget=forms.TextInput())
    second_name = forms.CharField(widget=forms.TextInput())
    age = forms.IntegerField(widget=forms.TextInput())
    class Meta:
        model = Persone
        fields = [
            'name',
            'second_name',
            'age',
            'phones'
            
        ]
        