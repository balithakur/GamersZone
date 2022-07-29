# Generated by Django 4.0.4 on 2022-07-04 05:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('firstapp', '0049_remove_freefiredata_id_freefiredata_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='paymentdata',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('status', models.CharField(max_length=30)),
                ('orderid', models.IntegerField()),
                ('date', models.IntegerField()),
            ],
        ),
    ]