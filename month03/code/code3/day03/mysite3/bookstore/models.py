from django.db import models

# Create your models here.
# class Book(models.Model):
#     title=models.CharField(max_length=30,db_index=True,null=False) #varchar(30)
#     price=models.DecimalField(decimal_places=2,max_digits=7,null=True,db_column='jiage') #decimal(7,2)
#     # social=models.CharField(max_length=30,verbose_name='出版社') #varchar(30)
#     market_price=models.DecimalField(max_digits=7,decimal_places=2) #varchar(30)
#     # 添加字段
#     # pub_date=models.DateField(auto_now_add=True)
#     pub=models.CharField(max_length=30,null=False)


class Book(models.Model):
    title = models.CharField(max_length=30, db_index=True, null=False)  # varchar(30)
    price = models.DecimalField(decimal_places=2, max_digits=7, null=True, db_column='jiage')  # decimal(7,2)
    market_price = models.DecimalField(max_digits=7, decimal_places=2)  # varchar(30)
    pub = models.CharField(max_length=30, null=False)


class Author(models.Model):
    name=models.CharField(max_length=30,db_index=True,null=False)
    age=models.IntegerField(null=False,default=1)
    email=models.EmailField(max_length=30,null=True)