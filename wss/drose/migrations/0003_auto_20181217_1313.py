# Generated by Django 2.1.2 on 2018-12-17 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drose', '0002_scanresult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scanresult',
            name='port',
            field=models.IntegerField(blank=True),
        ),
    ]