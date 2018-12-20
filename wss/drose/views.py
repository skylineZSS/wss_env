from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import PasswordChangeForm
from .forms import 自定义注册表单, 自定义编辑表单, 自定义登录表单
from .models import 普通会员表
from django.contrib.auth.decorators import login_required
from elasticsearch import Elasticsearch
from .collector.worker import *

# Create your views here.


def queryProcess(query):
    tmp = query.split(' ')
    print(tmp)
    meta = []
    query_dict = []
    for x in tmp:
        if x.count(':') == 0:
            query_dict.append(x)
        else:
            x = x.replace('+', ' ')
            meta = x.split(':')
            query_dict.append({meta[0]: meta[1]})
    return query_dict


def 主页(请求):
    if 请求.method == 'POST':
        query = 请求.POST.get('q')
        print(query)

        # 对搜索字段q进行解析
        query_dict = queryProcess(query)
        should_list = []
        must_list = []
        tmp = []
        for x in query_dict:
            if str(x).count(':') == 0:
                tmp = [
                    {'match': {'ip': x}},
                    {'match': {'port': x}},
                    {'match': {'state': x}},
                    {'match': {'cpe': x}},
                    {'match': {'name': x}},
                    {'match': {'proto': x}},
                    {'match': {'banners': x}},
                ]
                should_list.extend(tmp)
            else:
                must_list.append({'match': x})

        query_dsl = {
            'query': {
                'bool': {
                    'should': should_list,
                    'must': must_list
                }
            }
        }

        es = Elasticsearch("127.0.0.1:9200")
        responce = es.search(index="es_scanresult", body=query_dsl)
        data = responce["hits"]["hits"]

        return render(请求, 'drose/home.html', {'data': data})
    else:
        return render(请求, 'drose/home.html')


def 登录(请求):
    if 请求.method == 'POST':
        登录表单 = 自定义登录表单(data=请求.POST)
        if 登录表单.is_valid():
            用户 = authenticate(请求, username=登录表单.cleaned_data['username'], password=登录表单.cleaned_data['password'])
            login(请求, 用户)
            return redirect('drose:主页')
    else:
        登录表单 = 自定义登录表单()

    内容 = {'登录表单': 登录表单, '用户': 请求.user}
    return render(请求, 'drose/login.html', 内容)


def 登出(请求):
    logout(请求)
    return redirect('drose:主页')


def 注册(请求):
    if 请求.method == 'POST':
        注册表单 = 自定义注册表单(请求.POST)
        if 注册表单.is_valid():
            注册表单.save()
            用户 = authenticate(请求, username=注册表单.cleaned_data['username'], password=注册表单.cleaned_data['password1'])
            用户.email = 注册表单.cleaned_data['email']
            普通会员表(用户=用户, 昵称=注册表单.cleaned_data['昵称'], 生日=注册表单.cleaned_data['生日']).save()
            login(请求, 用户)
            return redirect('drose:主页')
    else:
        注册表单 = 自定义注册表单()

    内容 = {'注册表单': 注册表单}
    return render(请求, 'drose/register.html', 内容)


@login_required(login_url='drose:登录')
def 个人中心(请求):
    内容 = {'用户': 请求.user}
    return render(请求, 'drose/user_center.html', 内容)


@login_required(login_url='drose:登录')
def 编辑个人信息(请求):
    if 请求.method == 'POST':
        编辑表单 = 自定义编辑表单(请求.POST, instance=请求.user)
        if 编辑表单.is_valid():
            编辑表单.save()
            请求.user.普通会员表.昵称 =编辑表单.cleaned_data['昵称']
            请求.user.普通会员表.生日 =编辑表单.cleaned_data['生日']
            请求.user.普通会员表.save()
            return redirect('drose:个人中心')
    else:
        编辑表单 = 自定义编辑表单(instance=请求.user)

    内容 = {'编辑表单': 编辑表单, '用户': 请求.user}
    return render(请求, 'drose/edit_profile.html', 内容)


@login_required(login_url='drose:登录')
def 修改密码(请求):
    if 请求.method == 'POST':
        改密表单 = PasswordChangeForm(data=请求.POST, user=请求.user)
        if 改密表单.is_valid():
            改密表单.save()
            return redirect('drose:登录')
    else:
        改密表单 = PasswordChangeForm(data=请求.POST, user=请求.user)

    内容 = {'改密表单': 改密表单, '用户': 请求.user}
    return render(请求, 'drose/change_password.html', 内容)


def 使用说明(请求):
    return render(请求, 'drose/help.html')


def 人工标注指纹(请求):
    return render(请求, 'drose/manual_annotation.html')


def 先验指纹查询(请求):
    return render(请求, 'drose/prior_fingerprint_query.html')


def 未知协议查询(请求):
    return render(请求, 'drose/unknown_protocol_query.html')

def 扫描管理(请求):
    if 请求.method == 'POST':
        ip = 请求.POST['ip']
        port = 请求.POST['port']
        print(ip, port)
        Arguments = '-Pn -sS -T4 --script=banner -O'
        scanNetwork(ip, port, Arguments)
    # 内容 = {'改密表单': 改密表单, '用户': 请求.user}

    return render(请求, 'drose/scan_manage.html')
