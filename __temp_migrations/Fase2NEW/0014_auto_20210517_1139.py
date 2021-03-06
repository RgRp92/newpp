# Generated by Django 2.2.12 on 2021-05-17 09:39

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('Fase2NEW', '0013_auto_20210517_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='quiz',
            field=otree.db.models.StringField(blank=True, choices=[['1', '€ 20720'], ['0', '€ 21436'], ['2', '€ 18168']], default='', max_length=10000, null=True, verbose_name='In base alla figura mostrata, quale sarà il vostro guadagno se la variazione sarà del + 2%?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='quiz2',
            field=otree.db.models.StringField(blank=True, choices=[['1', '€ 20720'], ['0', '€ 21436'], ['2', '€ 18168']], default='', max_length=10000, null=True, verbose_name='In base alla figura mostrata quale sarà il vostro guadagno se la variazione sarà del +2%?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='quiz3',
            field=otree.db.models.StringField(blank=True, choices=[['0', '€ 20720'], ['1', '€ 19394'], ['2', '€ 25518']], default='', max_length=10000, null=True, verbose_name='In base alla figura mostrata quale sarà il vostro guadagno se la variazione sarà del - 8%?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='quiz4',
            field=otree.db.models.StringField(blank=True, choices=[['0', '€ 20720'], ['1', '€ 19394'], ['2', '€ 25518']], default='', max_length=10000, null=True, verbose_name='In base alla figura mostrata quale sarà il vostro guadagno se la variazione sarà del  -8%?'),
        ),
    ]
