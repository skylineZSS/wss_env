# Generated by Django 2.1.2 on 2018-12-17 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drose', '0003_auto_20181217_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='scanresult',
            name='banners',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
