# Generated by Django 4.0.6 on 2023-07-08 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_task_manager_app', '0002_auto_20220103_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('manager', 'Manager'), ('employee', 'Employee')], default=2, max_length=20),
            preserve_default=False,
        ),
    ]
