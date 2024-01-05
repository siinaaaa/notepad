from django.contrib import admin
from .models import Note


# Register your models here.

@admin.register(Note)
class AdminNote(admin.ModelAdmin):
    list_display = ['text']
