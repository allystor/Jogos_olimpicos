# Generated by Django 4.0.6 on 2022-07-18 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nova_competicao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competicao',
            name='local_da_competicao',
            field=models.CharField(choices=[('1', 'Arena Corinthians'), ('2', 'Maracanã')], max_length=100),
        ),
    ]
