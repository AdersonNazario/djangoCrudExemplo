from django import forms
from .models import Servico, Contact
from datetime import time

HOUR_CHOICES = [(time(hour=x), '{:02d}:00'.format(x)) for x in range(8, 16)]

class DateInput(forms.DateInput):
    input_type = 'date'

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
                'agendamento': DateInput(),
                'hora': forms.Select(choices=HOUR_CHOICES)
            }

