from django.contrib import admin
from .models import Note, Modify


# Register your models here.

@admin.register(Note)
class AdminNote(admin.ModelAdmin):
    list_display = ['text']


@admin.register(Modify)
class AdminModify(admin.ModelAdmin):
    list_display = ['number']
