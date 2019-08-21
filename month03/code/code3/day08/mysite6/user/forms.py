
from django import forms

class MyRegFrom(forms.Form):
    # 限定username 必须大于等于６个字符
    username = forms.CharField(label='用户名', initial="请填写",
                               required=False)
    password = forms.CharField(label='密码',
                               # widget=forms.PasswordInput,
                               required=False)
    password2 = forms.CharField(label="重复密码")

    def clean_username(self):
        '''此方法限定username必须大于等于６个字符'''
        uname = self.cleaned_data['username']
        if len(uname) < 6:
            raise forms.ValidationError("用户名太短")
        return uname

    def clean(self):
        '验证两个密码是否一致！不一致抛出ValidationError类型的异常'
        pwd1 = self.cleaned_data['password']
        pwd2 = self.cleaned_data['password2']
        if pwd1 != pwd2:
            raise forms.ValidationError("两次密码不一致")
        return self.cleaned_data
    # def clean_password(self):
    #     pwd1 = self.cleaned_data['password']
    #     if len(pwd1) == 0:
    #         raise forms.ValidationError("密码不能为空")
    #     return pwd1



