# Generated by Django 4.0.4 on 2022-05-22 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0007_account_pass5'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='mail',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]