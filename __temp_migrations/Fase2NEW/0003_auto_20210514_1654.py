# Generated by Django 2.2.12 on 2021-05-14 14:54

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('Fase2NEW', '0002_auto_20210514_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='quiz',
            field=otree.db.models.StringField(blank=True, choices=[['0', '12.28'], ['2', '9.78'], ['1', '16.53']], default='', max_length=10000, null=True, verbose_name='1. Avete scelto opzione A. In base alla figura mostrata quale sarà il vostro guadagno se la variazione sarà del + 2%'),
        ),
    ]