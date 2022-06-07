# Generated by Django 4.0.4 on 2022-05-22 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0014_alter_account_mail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='mail',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='name',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]