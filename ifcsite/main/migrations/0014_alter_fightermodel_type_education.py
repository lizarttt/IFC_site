# Generated by Django 4.0.1 on 2022-06-18 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_remove_fightermodel_typing_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fightermodel',
            name='type_education',
            field=models.CharField(choices=[('Лёгкий', 'light'), ('Средний', 'middle'), ('Полутяжёлый', 'heavywight')], max_length=20, verbose_name='Весовая'),
        ),
    ]
