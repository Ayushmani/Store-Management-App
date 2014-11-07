# import libraries
from django import forms
from django.forms import ModelForm

# import models
from StoreApp.models import Customer


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone_number', 'date_of_birth', 'address']
        widgets = {
            'name': forms.TextInput(attrs={
                'autofocus': 'autofocus', # Ithenthina use cheythennu valla idea undo??? If yes replace this comment
                'placeholder': 'Enter name of the customer',
                'class': 'form-control'
            }),
            'phone_number': forms.IntegerField(attrs={
                'placeholder': 'Enter phone number',
                'class': 'form-control'
            }),
            'date_of_birth': forms.DateField(attrs={
                'placeholder': 'Enter your date of birth',
                'class': 'form-control'
            }),
            'address': forms.TextInput(attrs={
                'placeholder': 'Enter your address',
                'class': 'form-control'
            }),

        }
