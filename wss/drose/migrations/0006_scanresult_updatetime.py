# Generated by Django 2.1.2 on 2018-12-18 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drose', '0005_auto_20181217_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='scanresult',
            name='updatetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]