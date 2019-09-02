from django.contrib import admin
from . import  models
# Register your models here.
class BookManager(admin.ModelAdmin):
    list_display = ['id','title','price','market_price','pub']
    list_display_links = ['id','title']
    list_filter = ['pub']
    search_fields = ['title','pub']
    list_editable = ['market_price']

# admin.site.register(models.Book)
admin.site.register(models.Book,BookManager)

class AuthorManager(admin.ModelAdmin):
    list_display = ['id','name','age']
    # list_display_links = ['age']不能和list_editable = ['age']的字段不能同时使用。
    list_editable = ['age']
admin.site.register(models.Author,AuthorManager)


class WifeManager(admin.ModelAdmin):
    list_display = ['id','name','age','author']
admin.site.register(models.Wife,WifeManager)


