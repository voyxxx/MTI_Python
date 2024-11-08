# Generated by Django 5.0.4 on 2024-05-02 17:16

import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='ФИО клиента')),
                ('number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region='RU')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Электронная почта')),
            ],
        ),
    ]
