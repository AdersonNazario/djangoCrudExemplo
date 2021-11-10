# Generated by Django 3.2.8 on 2021-11-09 22:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servico_text', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='phone',
            new_name='telefone',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='address',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='description',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='lastName',
        ),
        migrations.AddField(
            model_name='contact',
            name='agendamento',
            field=models.DateField(default=datetime.date.today, verbose_name='Data Agendamento'),
        ),
        migrations.AddField(
            model_name='contact',
            name='nome',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Nome'),
        ),
        migrations.AddField(
            model_name='contact',
            name='servico',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crudapp.servico'),
        ),
    ]
