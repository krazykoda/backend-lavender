# Generated by Django 5.1.7 on 2025-04-09 22:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_app', '0002_tasks_progress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='progress',
            field=models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
