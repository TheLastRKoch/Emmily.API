from django.contrib import admin

from .models import Word, WordList

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ['word','language','phonetic']

@admin.register(WordList)
class WordlistAdmin(admin.ModelAdmin):
    list_display = ['name','language','owner']