# Generated by Django 2.2.12 on 2021-05-14 15:00

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('Fase2NEW', '0006_auto_20210514_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='quiz',
            field=otree.db.models.StringField(blank=True, choices=[['0', '21435.55'], ['2', '18168.49'], ['1', '20720.34']], default='', max_length=10000, null=True, verbose_name='1. In base alla figura mostrata quale sarà il vostro guadagno se la variazione sarà del + 2%'),
        ),
        migrations.AlterField(
            model_name='player',
            name='quiz2',
            field=otree.db.models.StringField(blank=True, choices=[['0', '15311.11'], ['1', '18168.49'], ['2', '20720.34']], default='', max_length=10000, null=True, verbose_name='2.In base alla figura mostrata quale sarà il vostro guadagno se la variazione sarà del - 20%'),
        ),
    ]
