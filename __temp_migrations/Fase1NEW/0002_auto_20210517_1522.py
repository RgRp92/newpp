# Generated by Django 2.2.12 on 2021-05-17 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Fase1NEW', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='rep_1',
        ),
        migrations.RemoveField(
            model_name='player',
            name='rep_2',
        ),
    ]
