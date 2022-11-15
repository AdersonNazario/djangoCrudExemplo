from rest_framework import serializers
from .models import Contact

class ContactSerializer(serializers.ModelSerializer):
    servico = serializers.ReadOnlyField(source='servico.servico_text')
    class Meta:
        model = Contact
        fields = ['nome', 'telefone', 'servico', 'agendamento', 'hora', 'author']

