# Generated by Django 4.0.1 on 2022-06-18 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_fightermodel_typing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fightermodel',
            name='typing',
        ),
        migrations.AddField(
            model_name='fightermodel',
            name='type_education',
            field=models.CharField(choices=[('light', 'Легкий'), ('middle', 'Средний вес'), ('light heavy', 'Полутяжёлый вес')], default=1, max_length=20, verbose_name='Весовая'),
            preserve_default=False,
        ),
    ]
