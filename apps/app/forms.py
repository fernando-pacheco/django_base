from django import forms
from .models import Fotografia

class FotografiaForms(forms.ModelForm):
    class Meta:
        model = Fotografia
        exclude = ['publicada']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'legenda': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'data_fotografia': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
        }
        
