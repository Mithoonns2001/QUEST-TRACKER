# Generated by Django 4.0.6 on 2023-07-10 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quest_track_app', '0007_user_assigned_manager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='assigned_manager',
        ),
    ]
