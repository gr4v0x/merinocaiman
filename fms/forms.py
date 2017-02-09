from django.forms import ModelForm, TextInput, Select
from .models import MainIden

class MainIdenForm(ModelForm):
    class Meta:
        model = MainIden
        fields = [
            'lastName', 'firstName', 'otherName',
            'gender', 'dateOfBirth', 'cityOfBirth',
            'countryOfBirth',
        ]
        widgets = {
            'lastName': TextInput(attrs={'class': 'form-control'}),
            'firstName': TextInput(attrs={'class': 'form-control'}),
            'otherName': TextInput(attrs={'class': 'form-control'}),
            'gender': Select(attrs={'class': 'form-control custom'})
        }
