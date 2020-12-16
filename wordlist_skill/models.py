from django.db import models

class Word(models.Model):
    word = models.CharField(max_length=100)
    phonetic = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    definition = models.TextField(max_length=100, blank=True)
    example = models.TextField(max_length=100, blank=True)
