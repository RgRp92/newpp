# Generated by Django 2.2.12 on 2021-06-03 08:22

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('Fase1NEW', '0028_auto_20210528_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='quiz2f1',
            field=otree.db.models.StringField(choices=[['2', '19.06 €'], ['2', '14.06 €'], ['1', '11.56 €']], default='', max_length=10000, null=True, verbose_name='1. In base alla figura mostrata quale sarà il suo guadagno se il reddito varierà tra +1% e +10%?'),
        ),
        migrations.AlterField(
            model_name='player',
            name='quizf1',
            field=otree.db.models.StringField(choices=[['2', '19.06 €'], ['2', '14.06 €'], ['1', '11.56 €']], default='', max_length=10000, null=True, verbose_name='1. In base alla figura mostrata quale sarà il suo guadagno se il reddito varierà tra +1% e +10%?'),
        ),
    ]
