# Generated by Django 3.0.7 on 2020-07-31 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('dt', models.DateTimeField()),
                ('desc', models.CharField(max_length=100)),
            ],
        ),
    ]
