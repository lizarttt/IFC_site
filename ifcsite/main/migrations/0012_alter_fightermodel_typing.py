# Generated by Django 4.0.1 on 2022-06-17 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_fightermodel_typing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fightermodel',
            name='typing',
            field=models.CharField(max_length=12, verbose_name='Весовая Легкий/Средний/Полутяжёлый. Писать один вариант'),
        ),
    ]
