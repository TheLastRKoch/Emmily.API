from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Word
from .serializers import WordSerializer
from rest_framework.exceptions import ValidationError

#region Word
@api_view(['GET'])
def getWords(request):
    words = Word.objects.all()
    serializer = WordSerializer(words, many=True)
    return Response (serializer.data)

@api_view(['POST'])
def addNewWord(request):
    serializer = WordSerializer(data=request.data)
    if Word.objects.filter(word = request.data['word']).count() > 0:
        raise ValidationError({'detail': 'The requested word already exist on the DB'})
    if serializer.is_valid():
        serializer.save()
    return Response (serializer.data)

@api_view(['GET','PUT','DELETE'])
def WordRetriveUpdateDestroy(request,id):
    if request.method == 'GET':
        word = Word.objects.get(id=id)
        serializer = WordSerializer(word, many=False)
        return Response (serializer.data)

    if request.method == 'PUT':
        word = Word.objects.get(id=id)
        serializer = WordSerializer(instance=word,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response (serializer.data)
    
    if request.method == 'DELETE':
        word = Word.objects.get(id=id)
        word.delete()
        return Response({'detail': 'Word deleted successfully'})
#endregion
