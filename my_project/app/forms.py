from django import forms
from .models import Lead


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ('name', 'phone')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'name',
                'placeholder': "Ваше имя"
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'phone',
                'placeholder': "Ваш номер телефона"
            }),
        }
