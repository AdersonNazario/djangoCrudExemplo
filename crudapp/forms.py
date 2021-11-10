from django import forms
from .models import Servico, Contact


class DateInput(forms.DateInput):
    input_type = 'date'

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
                'agendamento': DateInput(),
            }
