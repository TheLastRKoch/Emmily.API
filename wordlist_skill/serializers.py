from rest_framework import serializers

from wordlist_skill.models import Word

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ('word','phonetic','language','definition','example')
        
