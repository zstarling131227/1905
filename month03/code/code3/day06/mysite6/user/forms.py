from django import forms


class RegForm(forms.Form):
    username = forms.CharField(max_length=30, label='请输入用户名')
    password = forms.CharField(max_length=30, label='请输入密码')
    password2 = forms.CharField(max_length=20, label='请再次输入密码')
