# Generated by Django 4.2.3 on 2023-07-18 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_rename_proyecto_bicicleta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bicicleta',
            name='precio_usd',
        ),
        migrations.AlterField(
            model_name='bicicleta',
            name='precio',
            field=models.TextField(max_length=200),
        ),
    ]
