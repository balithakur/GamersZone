# Generated by Django 4.0.4 on 2022-06-19 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0045_duofftournament'),
    ]

    operations = [
        migrations.CreateModel(
            name='squadfftournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=30)),
                ('totalplayer', models.CharField(max_length=10)),
                ('time', models.CharField(max_length=30)),
                ('prize', models.CharField(max_length=30)),
            ],
        ),
    ]
