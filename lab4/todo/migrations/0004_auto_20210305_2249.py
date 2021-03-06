# Generated by Django 3.1.7 on 2021-03-05 16:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20210305_2226'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='todo',
            name='creation_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
