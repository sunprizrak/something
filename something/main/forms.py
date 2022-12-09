from django import forms
from .models import Contacts


class ContactsForm(forms.ModelForm):

    class Meta:
        model = Contacts
        fields = '__all__'
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'email',
                'required': True,
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя',
                'required': True,
            }),
            'phone_number': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона',
                'required': True,
            }),
            'object_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Наименование объекта',
                'required': True,
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'placeholder': 'дд.мм.гггг',
                'required': True,
            }),
        }