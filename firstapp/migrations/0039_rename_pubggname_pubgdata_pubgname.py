# Generated by Django 4.0.4 on 2022-06-17 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0038_rename_pubgname_pubgdata_pubggname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pubgdata',
            old_name='pubggname',
            new_name='pubgname',
        ),
    ]
