# Generated by Django 2.1.2 on 2018-12-18 07:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('drose', '0006_scanresult_updatetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scanresult',
            name='updatetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
