# Generated by Django 4.0.4 on 2022-06-13 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0025_alter_freefiredata_freefireid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='freefiredata',
            old_name='freefireid',
            new_name='ffid',
        ),
        migrations.RenameField(
            model_name='freefiredata',
            old_name='freefirename',
            new_name='ffname',
        ),
    ]
