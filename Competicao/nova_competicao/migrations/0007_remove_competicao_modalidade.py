# Generated by Django 4.0.6 on 2022-07-18 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nova_competicao', '0006_alter_competicao_data_alter_competicao_hora'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='competicao',
            name='modalidade',
        ),
    ]
