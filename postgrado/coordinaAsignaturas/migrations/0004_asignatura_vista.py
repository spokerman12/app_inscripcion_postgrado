# Generated by Django 2.0.4 on 2018-06-09 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coordinaAsignaturas', '0003_auto_20180606_1916'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignatura',
            name='vista',
            field=models.BooleanField(default=False),
        ),
    ]
