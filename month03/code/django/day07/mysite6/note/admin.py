from django.contrib import admin

# Register your models here.

# note/admin.py
class NoteManager(admin.ModelAdmin):
    list_display = ['id', 'title', 'user']

from . import models
admin.site.register(models.Note, NoteManager)


