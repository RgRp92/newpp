# Generated by Django 2.2.12 on 2021-05-22 09:32

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('Fase2NEW', '0021_auto_20210520_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='HL_13',
        ),
        migrations.AlterField(
            model_name='player',
            name='quiz',
            field=otree.db.models.StringField(blank=True, choices=[['1', '18403 €'], ['2', '16361 €'], ['2', '21436 €']], default='', max_length=10000, null=True, verbose_name='In base alla figura mostrata, quale sarà il vostro guadagno se la variazione sarà del + 2%?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='quiz2',
            field=otree.db.models.StringField(blank=True, choices=[['1', '18403 €'], ['2', '16361 €'], ['2', '21436 €']], default='', max_length=10000, null=True, verbose_name='In base alla figura mostrata quale sarà il vostro guadagno se la variazione sarà del +2%?'),
        ),
    ]
