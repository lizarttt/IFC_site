# Generated by Django 4.0.1 on 2022-06-17 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_fightermodel_typing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fightermodel',
            name='typing',
            field=models.PositiveSmallIntegerField(choices=[('Другое', 'Легкий вес'), (2, 'Средний вес'), (3, 'Полутяжелый вес')], verbose_name='Тип'),
        ),
    ]
