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


    def __str__(self):
        return "书名："+self.title
    class Meta:
        # 将数据库的bookstore_book表名改为'mybook'
        db_table='mybook'
        ##将类名book定义的显示改为下列字符（后台管理时显示）
        # verbose_name='boooooooooook'
        ##自带复数名是加s，此时是直接替换（后台管理时显示）
        # verbose_name_plural='booooookkook'



class Author(models.Model):
    name=models.CharField(max_length=30,
                          db_index=True,
                          verbose_name="作者姓名",
                          null=False)
    age=models.IntegerField(null=False,
                            default=1,
                            verbose_name="作者年龄")
    email=models.EmailField(null=True,
                            verbose_name="作者邮箱",
                            default='xxx@tedu.cn')

    def __str__(self):
        return "作者："+self.name

    # class Meta:
    #     db_name="myauthor"


class Wife(models.Model):
    name=models.CharField(max_length=30,verbose_name="妻子姓名")
    age=models.IntegerField(verbose_name="妻子年龄")
    author=models.OneToOneField(Author)

    def __str__(self):
        return "妻子："+self.name


























