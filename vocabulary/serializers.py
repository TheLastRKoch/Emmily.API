from rest_framework import serializers
from vocabulary.models import Word
from Emmily.services import DictionaryEn

class WordSerializer(serializers.ModelSerializer):

    phonetic = serializers.CharField(read_only=True)
    definition = serializers.CharField(read_only=True)
    urban_definition = serializers.CharField(read_only=True)
    example = serializers.CharField(read_only=True)
    class Meta:
        model = Word
        fields = ('id','word','language','phonetic','definition','urban_definition','example')

    def create(self, instance):
        dic = DictionaryEn(instance['word'])
        custom_phonetic = dic.getPhonetic()
        custom_definition = dic.getDefinition()
        custom_urban_definition = dic.getUrbanDefinition()
        custom_example =  dic.getSentence()

        if "Error" not in custom_phonetic:
            instance['phonetic'] = custom_phonetic
        else: 
            # Log in here
            pass

        if "Error" not in custom_definition:
            instance['definition'] = custom_definition
        else: 
            # Log in here
            pass

        if "Error" not in custom_urban_definition:
            instance['urban_definition'] = custom_urban_definition
        else: 
            # Log in here
            pass

        if "Error" not in custom_example:
            instance['example'] = custom_example
        else: 
            # Log in here
            pass
        
        return super().create(instance)


class WordListSerializer(serializers.ModelSerializer):
    pass