# Generated by Django 3.1.6 on 2021-02-17 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_auto_20210217_1724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='questions',
        ),
    ]
