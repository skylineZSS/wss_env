from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone as timezone

# Create your models here.


class 普通会员表(models.Model):
    用户 = models.OneToOneField(User, on_delete=models.CASCADE)
    昵称 = models.CharField(blank=True, max_length=50)
    生日 = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name_plural = '普通会员表'

class scanresult(models.Model):
    ip = models.CharField(max_length=30)
    port = models.IntegerField()
    proto = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=30, blank=True)
    cpe = models.CharField(max_length=30, blank=True)
    name = models.CharField(max_length=30, blank=True)
    banners = models.TextField(blank=True)
    product = models.TextField(blank=True)
    version = models.CharField(max_length=30, blank=True)
    extrainfo=models.TextField(blank=True)
    os_type = models.TextField(blank=True)
    updatetime = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = '扫描结果'

class ipaddress(models.Model):
    ip = models.CharField(max_length=30)
    continent = models.CharField(max_length=50, blank=True)
    country_name = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    latitude = models.CharField(max_length=50, blank=True)
    longitude= models.CharField(max_length=50, blank=True)
    updatetime = models.DateTimeField(default=timezone.now)

