# Generated by Django 4.2 on 2023-05-02 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidato', '0007_alter_candidato_certificacion_choferes_operadores_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidato',
            name='centro_de_costo',
            field=models.CharField(blank=True, choices=[('1', ''), ('1', ''), ('1', ''), ('1', ''), ('1', ''), ('1', ''), ('1', ''), ('1', '')], max_length=30, null=True),
        ),
    ]