# Generated by Django 3.0.7 on 2020-08-11 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='affiliateregister',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='sellerregister',
            name='email',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]
