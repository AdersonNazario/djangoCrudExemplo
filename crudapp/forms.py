from django import forms
from .models import Servico, Contact, CustomUser
from datetime import time
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


HOUR_CHOICES = [(time(hour=x), '{:02d}:00'.format(x)) for x in range(8, 16)]

class DateInput(forms.DateInput):
    input_type = 'date'

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        exclude = ['author']
        widgets = {
                'agendamento': DateInput(),
                'hora': forms.Select(choices=HOUR_CHOICES)
            }

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")
        username = forms.CharField(label='Nome do Usuário', min_length=5, max_length=150)  
        email = forms.EmailField(label='email')  

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("username", "email")
        username = forms.CharField(label='Nome do Usuário', min_length=5, max_length=150)  
        email = forms.EmailField(label='email')  

