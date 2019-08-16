from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Publisher)
admin.site.register(models.Book2)
class Author3Manager(admin.ModelAdmin):
    list_filter = ['name']
    list_display = ['id', 'name']
admin.site.register(models.Author3,Author3Manager)
class Book3Manager(admin.ModelAdmin):
    list_filter = ['title']
    list_display = ['id','title']
admin.site.register(models.Book3,Book3Manager)