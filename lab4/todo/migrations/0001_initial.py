# Generated by Django 3.1.7 on 2021-03-05 14:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=255)),
                ('creation_date', models.DateField(default=datetime.datetime(2021, 3, 5, 20, 51, 28, 920774))),
                ('due_on_date', models.DateField()),
                ('owner', models.CharField(default='owner', max_length=50)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]