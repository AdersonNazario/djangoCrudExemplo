from django.db import models
from datetime import date
# Create your models here.


class Servico(models.Model):
    servico_text = models.CharField(max_length=200)
    # pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.servico_text


class Contact(models.Model):
    nome = models.CharField("Nome", max_length=255, blank = True, null = True)
    # lastName = models.CharField("Last name", max_length=255, blank = True, null = True)
    # email = models.EmailField()
    telefone = models.CharField(max_length=20, blank = True, null = True)
    # address = models.TextField(blank=True, null=True)
    # description = models.TextField(blank=True, null=True)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, null=True)
    agendamento = models.DateField('Data Agendamento', default=date.today)
    createdAt = models.DateTimeField("Created At", auto_now_add=True)
    
    def __str__(self):
        return self.nome
