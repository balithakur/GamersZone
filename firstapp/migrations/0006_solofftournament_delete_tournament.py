# Generated by Django 4.0.4 on 2022-05-17 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_tournament'),
    ]

    operations = [
        migrations.CreateModel(
            name='solofftournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=30)),
                ('totalplayer', models.CharField(max_length=10)),
                ('time', models.CharField(max_length=30)),
                ('prize', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='tournament',
        ),
    ]
