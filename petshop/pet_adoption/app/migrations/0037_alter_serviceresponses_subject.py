# Generated by Django 4.0.3 on 2022-11-26 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0036_serviceresponses_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceresponses',
            name='subject',
            field=models.CharField(max_length=100),
        ),
    ]
