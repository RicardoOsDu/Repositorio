# Generated by Django 4.2 on 2023-04-18 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidato', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidato',
            name='correo',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
