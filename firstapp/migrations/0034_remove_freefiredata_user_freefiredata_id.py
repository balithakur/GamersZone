# Generated by Django 4.0.4 on 2022-06-16 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0033_remove_freefiredata_id_freefiredata_user'),
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
