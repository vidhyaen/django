# Generated by Django 3.0.7 on 2020-08-01 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_remove_todo_user_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo_user',
            old_name='task',
            new_name='user',
        ),
    ]
