# Generated by Django 2.2.12 on 2021-05-17 14:46

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('Fase1NEW', '0002_auto_20210517_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='quiz',
            field=otree.db.models.StringField(blank=True, choices=[['0', '12.44'], ['2', '14.94'], ['1', '13.69']], default='', max_length=10000, null=True, verbose_name='1. In base alla figura mostrata quale sarà il vostro guadagno se il reddito varierà del + 2%'),
        ),
        migrations.AlterField(
            model_name='player',
            name='quiz2',
            field=otree.db.models.StringField(blank=True, choices=[['0', '17.44'], ['1', '14.94'], ['2', '13.69']], default='', max_length=10000, null=True, verbose_name='2.In base alla figura mostrata quale sarà il vostro guadagno se il reddito varierà del - 25%'),
        ),
    ]
