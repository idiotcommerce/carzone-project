# Generated by Django 4.2.1 on 2023-06-01 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_alter_car_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
