# Generated by Django 2.1.2 on 2018-12-15 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drose', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='scanresult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(blank=True, max_length=30)),
                ('port', models.IntegerField(blank=True, max_length=30)),
                ('cpe', models.CharField(blank=True, max_length=30)),
                ('name', models.CharField(blank=True, max_length=30)),
                ('product', models.CharField(blank=True, max_length=30)),
                ('proto', models.CharField(blank=True, max_length=30)),
                ('state', models.CharField(blank=True, max_length=30)),
                ('version', models.CharField(blank=True, max_length=30)),
            ],
            options={
                'verbose_name_plural': '扫描结果',
            },
        ),
    ]