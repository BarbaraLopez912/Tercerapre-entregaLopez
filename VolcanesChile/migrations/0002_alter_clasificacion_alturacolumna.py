# Generated by Django 4.2.7 on 2023-11-26 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VolcanesChile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clasificacion',
            name='alturacolumna',
            field=models.IntegerField(),
        ),
    ]