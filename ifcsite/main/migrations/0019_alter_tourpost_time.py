# Generated by Django 4.0.1 on 2022-06-29 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_postfightermodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourpost',
            name='time',
            field=models.TimeField(verbose_name='Время'),
        ),
    ]
