from django.db import models
from django.contrib.auth.models import User

class Word(models.Model):
    id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    phonetic = models.CharField(max_length=100, blank=True)
    definition = models.TextField(max_length=256, blank=True)
    urban_definition = models.TextField(max_length=256, blank=True)
    example = models.TextField(max_length=256, blank=True)

    def __str__(self):
        return self.word

class Wordlist(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    words = models.ManyToManyField(Word)

