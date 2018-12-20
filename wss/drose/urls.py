from django.urls import path
from . import views

app_name = 'drose'
urlpatterns = [
    path('', views.主页, name='主页'),
    path('login/', views.登录, name='登录'),
    path('logout/', views.登出, name='登出'),
    path('register/', views.注册, name='注册'),
    path('user_center/', views.个人中心, name='个人中心'),
    path('help/', views.使用说明, name='使用说明'),
    path('user_center/edit_profile', views.编辑个人信息, name='编辑个人信息'),
    path('user_center/change_password', views.修改密码, name='修改密码'),
    path('manual_annotation', views.人工标注指纹, name='人工标注指纹'),
    path('prior_fingerprint_query', views.先验指纹查询, name='先验指纹查询'),
    path('unknown_protocol_query', views.未知协议查询, name='未知协议查询'),
    path('scan_manage', views.扫描管理, name='扫描管理'),
]
