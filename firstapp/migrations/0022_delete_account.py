# Generated by Django 4.0.4 on 2022-05-26 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0021_alter_account_mail'),
    ]

    operations = [
        migrations.DeleteModel(
            name='account',
        ),
    ]