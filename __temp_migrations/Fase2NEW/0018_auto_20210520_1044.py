# Generated by Django 2.2.12 on 2021-05-20 08:44

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('Fase2NEW', '0017_auto_20210520_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='quiz',
            field=otree.db.models.StringField(blank=True, choices=[['1', '20574 €'], ['2', '18533 €'], ['2', '21436 €']], default='', max_length=10000, null=True, verbose_name='In base alla figura mostrata, quale sarà il vostro guadagno se la variazione sarà del + 2%?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='quiz2',
            field=otree.db.models.StringField(blank=True, choices=[['1', '20574 €'], ['2', '18533 €'], ['2', '21436 €']], default='', max_length=10000, null=True, verbose_name='In base alla figura mostrata quale sarà il vostro guadagno se la variazione sarà del +2%?'),
        ),
    ]