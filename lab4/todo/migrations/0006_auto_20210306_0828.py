# Generated by Django 3.1.7 on 2021-03-06 02:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_todo_list'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='list',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='todo',
            old_name='task',
            new_name='name',
        ),
    ]
