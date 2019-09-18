from django.db import models


# Create your models here.

# 一对多：出版社是一对多中的一
class Publisher(models.Model):
    name = models.CharField(verbose_name='出版社名称', max_length=30, unique=True)

    def __str__(self):
        return "出版社：" + self.name


class Book2(models.Model):
    title = models.CharField(verbose_name="书名", max_length=30)
    publisher = models.ForeignKey(Publisher, null=True)

    def __str__(self):
        return "书名：" + self.title


# 多对多
class Author3(models.Model):
    name = models.CharField(verbose_name='作者名称', max_length=30)

    def __str__(self):
        return "作者：" + self.name


class Book3(models.Model):
    title = models.CharField(verbose_name="书名", max_length=30)
    authors = models.ManyToManyField(Author3)

    def __str__(self):
        return "书名：" + self.title
