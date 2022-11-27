# Generated by Django 4.0.3 on 2022-09-28 19:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='pet_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='breed_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('petCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product_category')),
            ],
        ),
        migrations.CreateModel(
            name='Adopt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('birthdate', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=10000)),
                ('age', models.IntegerField()),
                ('Breed', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.breed_category')),
                ('petCategory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.pet_category')),
            ],
        ),
    ]
