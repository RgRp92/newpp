# Generated by Django 2.2.12 on 2021-05-23 21:12

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('Fase1NEW', '0014_auto_20210523_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='rip1',
            field=otree.db.models.StringField(blank=True, choices=[['0', 'Penso che questa allocazione rispecchi accuratamente la mia opinione, non voglio procedere con altre allocazioni'], ['1', 'Voglio procedere con ancora una scelta']], default='', max_length=10000, null=True, verbose_name=''),
        ),
        migrations.AlterField(
            model_name='player',
            name='rip2',
            field=otree.db.models.StringField(blank=True, choices=[['0', 'Penso che questa allocazione rispecchi accuratamente la mia opinione, non voglio procedere con altre allocazioni'], ['1', 'Voglio procedere con ancora una scelta']], default='', max_length=10000, null=True, verbose_name=''),
        ),
    ]