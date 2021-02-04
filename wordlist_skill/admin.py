from django.contrib import admin

from .models import Word, Wordlist

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ['id','word','language','phonetic']

@admin.register(Wordlist)
class WordlistAdmin(admin.ModelAdmin):
    list_display = ['id','name','language','owner']