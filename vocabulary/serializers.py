from rest_framework import serializers
from django.contrib.auth.models import User
from Emmily.services import DictionaryEn
from vocabulary.models import Word, WordList

class WordSerializer(serializers.ModelSerializer):

    phonetic = serializers.CharField(read_only=True)
    definition = serializers.CharField(read_only=True)
    urban_definition = serializers.CharField(read_only=True)
    example = serializers.CharField(read_only=True)
    class Meta:
        model = Word
        fields = fields = '__all__'
        depth = 1

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

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','username','email')
        model = User

class WordListSerializer(serializers.ModelSerializer):
    
    def create(self, instance):
        return super().create(instance)

    def update(self,instance, validated_data):
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["owner"] = OwnerSerializer(instance.owner).data
        return representation

    class Meta:
        model = WordList
        fields = fields = '__all__'
        depth = 1