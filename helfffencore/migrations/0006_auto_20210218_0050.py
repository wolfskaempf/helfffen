# Generated by Django 3.1.6 on 2021-02-17 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helfffencore', '0005_auto_20210217_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helpoffer',
            name='additional_information',
            field=models.TextField(blank=True),
        ),
    ]
