# Generated by Django 2.2.12 on 2021-05-21 13:25

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('Fase1NEW', '0010_auto_20210521_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='pref3',
            field=otree.db.models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0, null=True, verbose_name=''),
        ),
    ]
