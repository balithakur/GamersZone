# Generated by Django 4.0.4 on 2022-06-16 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0035_remove_freefiredata_id_freefiredata_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='freefiredata',
            name='user',
        ),
        migrations.AddField(
            model_name='freefiredata',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
