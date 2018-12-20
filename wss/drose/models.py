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
    cpe = models.CharField(max_length=30, blank=True)
    name = models.CharField(max_length=30, blank=True)
    product = models.CharField(max_length=30, blank=True)
    proto = models.CharField(max_length=30, blank=True)
    state = models.CharField(max_length=30, blank=True)
    version = models.CharField(max_length=30, blank=True)
    operation = models.TextField(blank=True)
    banners = models.TextField(blank=True)
    updatetime = models.DateTimeField(default=timezone.now)



    class Meta:
        verbose_name_plural = '扫描结果'


