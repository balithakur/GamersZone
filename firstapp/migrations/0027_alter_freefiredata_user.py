# Generated by Django 4.0.4 on 2022-06-13 06:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('firstapp', '0026_rename_freefireid_freefiredata_ffid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freefiredata',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]