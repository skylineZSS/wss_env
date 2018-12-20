from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
# from captcha.fields import CaptchaField


class 自定义登录表单(AuthenticationForm):
    # 验证码 = CaptchaField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].error_messages = {'invalid_login': '用户名不存在', 'required': '用户名不能为空'}
        self.fields['password'].error_messages = {'invalid_login': '密码不正确', 'required': '密码不能为空'}

class 自定义注册表单(UserCreationForm):
    昵称 = forms.CharField(required=False, max_length=50)
    生日 = forms.DateField(required=False)
    # 验证码 = CaptchaField()

    class Meta:
        model = User
        fields = ('username','password1','password2','email','昵称','生日')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].error_messages = {'unique': '用户名已存在', 'invalid': '格式不正确'}


class 自定义编辑表单(UserChangeForm):
    昵称 = forms.CharField(required=False, max_length=50)
    生日 = forms.DateField(required=False)

    class Meta:
        model = User
        fields = ('username', 'email', '昵称', '生日')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].error_messages = {'unique': '用户名已存在', 'invalid': '格式不正确'}

# class 自定义扫描表单(AuthenticationForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['ip'].error_messages = {'invalid_login': '用户名不存在', 'required': '用户名不能为空'}
#         self.fields['port'].error_messages = {'invalid_login': '密码不正确', 'required': '密码不能为空'}