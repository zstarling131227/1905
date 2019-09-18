from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=30,
                             null=False,
                             unique=True,
                             verbose_name="书名")
    price = models.DecimalField(decimal_places=2,
                                max_digits=7,
                                verbose_name="定价",
                                default="99999")
    market_price = models.DecimalField(max_digits=7,
                                       decimal_places=2,
                                       verbose_name="零售价格",
                                       default="99999")
    pub = models.CharField(max_length=30,
                           null=True,
                           verbose_name="出版社")


class Author(models.Model):
    name=models.CharField(max_length=30,
                          db_index=True,
                          verbose_name="作者姓名",
                          null=False)
    age=models.IntegerField(null=False,
                            default=1,
                            verbose_name="作者年龄")
    email=models.EmailField(null=True,
                            verbose_name="作者邮箱")

