# Generated by Django 3.1.6 on 2021-02-17 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helfffencore', '0002_auto_20210217_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='deadline',
            field=models.DateField(blank=True, null=True),
        ),
    ]
