# Generated by Django 3.0.7 on 2020-08-12 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productlist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producttable',
            name='url',
            field=models.ImageField(max_length=255, upload_to=''),
        ),
    ]
