# Generated by Django 2.2.12 on 2021-05-20 11:58

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('Fase1NEW', '0004_auto_20210519_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='quiz3f1',
            field=otree.db.models.StringField(blank=True, choices=[['0', '17.44'], ['1', '14.94'], ['2', '13.69']], default='', max_length=10000, null=True, verbose_name='2. In base alla figura mostrata quale sarà il vostro guadagno se il reddito varierà del - 25%'),
        ),
        migrations.AlterField(
            model_name='player',
            name='quiz4f1',
            field=otree.db.models.StringField(blank=True, choices=[['0', '17.44'], ['1', '14.94'], ['2', '13.69']], default='', max_length=10000, null=True, verbose_name='2. In base alla figura mostrata quale sarà il vostro guadagno se il reddito varierà del - 25%'),
        ),
    ]