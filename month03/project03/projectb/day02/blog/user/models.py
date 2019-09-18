from django.db import models


# Create your models here.
class UserProfiles(models.Model):
    username = models.CharField(max_length=11, primary_key=True, verbose_name='用户名')
    nickname = models.CharField(max_length=30, default=username, verbose_name='昵称')
    email = models.CharField(max_length=50, verbose_name='邮箱', null=True)
    password = models.CharField(max_length=32, verbose_name='密码')
    sign = models.CharField(max_length=50, verbose_name='个性签名')
    info = models.CharField(max_length=150, verbose_name='个人描述')
    avatar = models.ImageField(upload_to='avatar/')

    class Meta:
        db_table = 'user_profile'
