# Generated by Django 4.0.3 on 2022-09-28 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_breed_category_petcategory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adopt',
            name='birthdate',
        ),
    ]
