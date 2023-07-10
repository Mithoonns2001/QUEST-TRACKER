# Generated by Django 4.0.6 on 2023-07-09 07:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_task_manager_app', '0003_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='complete',
            name='status',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('manager', 'Manager'), ('employee', 'Employee'), ('head', 'Head')], max_length=20),
        ),
    ]
