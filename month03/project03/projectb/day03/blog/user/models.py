from django.db import models


# Create your models here.

# class -> UserProfile
# 表名 user_profile
# username, nickname,email,password,sign,info,avatar

# CharField字段不建议使用null=True，因为会占空间，可能会影响索引效率
class UserProfile(models.Model):
    username = models.CharField(max_length=11, verbose_name='用户名', primary_key=True)
    nickname = models.CharField(max_length=30, verbose_name='昵称')
    email = models.CharField(max_length=50, verbose_name='邮箱', null=True)
    password = models.CharField(max_length=32)
    sign = models.CharField(max_length=50, verbose_name='个性签名')
    info = models.CharField(max_length=150, verbose_name='个人描述')
    avatar = models.ImageField(upload_to='avatar/')

    class Meta:
        db_table = 'user_profile'
