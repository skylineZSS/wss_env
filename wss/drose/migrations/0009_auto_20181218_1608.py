# Generated by Django 2.1.2 on 2018-12-18 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drose', '0008_auto_20181218_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scanresult',
            name='ip',
            field=models.CharField(max_length=30),
        ),
    ]
