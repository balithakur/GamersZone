# Generated by Django 4.0.4 on 2022-05-22 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0008_alter_account_mail'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='pass1',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
