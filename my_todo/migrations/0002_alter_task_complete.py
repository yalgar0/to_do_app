# Generated by Django 4.2.1 on 2023-07-24 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='complete',
            field=models.BooleanField(default=True),
        ),
    ]
