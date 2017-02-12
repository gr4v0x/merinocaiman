from django.forms import ModelForm, TextInput, Select
from .models import MainIden, NoteBook

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
            'gender': Select(attrs={'class': 'form-control custom'}),
            'dateOfBirth': TextInput(attrs={'class': 'form-control'}),
            'cityOfBirth': TextInput(attrs={'class': 'form-control'}),
            'countryOfBirth': Select(attrs={'class': 'form-control custom'})
        }

class AddNoteForm(ModelForm):
    class Meta:
        model = NoteBook
        fields = [
            'subject', 'noteDate', 'noteTime', 'note',
            'noteKey',
        ]
        widgets = {
            'subject': TextInput(attrs={'class': 'form-control'}),
            'note': TextInput(attrs={'class': 'form-control memo-field'}),
        }
