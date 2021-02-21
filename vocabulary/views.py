from rest_framework.exceptions import ValidationError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Word, WordList
from .serializers import WordSerializer, WordListSerializer

#region Word
@api_view(['GET','POST'])
def word_list_add(request):
    """Get the a list of the saved words"""
    if request.method == 'GET':
        words = Word.objects.all()
        serializer = WordSerializer(words, many=True)
        return Response (serializer.data)

    if request.method == 'POST':
        serializer = WordSerializer(data=request.data)
        if Word.objects.filter(word = request.data['word']).count() > 0:
            raise ValidationError({'detail': 'The requested word already exist on the DB'})
        if serializer.is_valid():
            serializer.save()
        return Response (serializer.data)

@api_view(['GET','PUT','DELETE'])
def word_retrive_update_destroy(request,id):
    """Perform the get update and delete functions"""
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

#region WordList
@api_view(['GET','POST'])
def wordlist_list_add(request):
    """Get the a list of the saved words"""
    if request.method == 'GET':
        wordlists = WordList.objects.all()
        serializer = WordListSerializer(wordlists, many=True)
        return Response (serializer.data)
    
    if request.method == 'POST':
        serializer = WordListSerializer(data=request.data)
        if WordList.objects.filter(name = request.data['name']).count() > 0:
            raise ValidationError({'detail': 'The requested wordlist already exist on the DB'})
        if serializer.is_valid():
            serializer.save()
        return Response (serializer.data)

@api_view(['GET','PUT','DELETE'])
def wordlist_retrive_update_destroy(request,id):
    """Perform the get update and delete functions"""
    if request.method == 'GET':
        wordlist = WordList.objects.get(id=id)
        serializer = WordListSerializer(wordlist, many=False)
        return Response (serializer.data)

    if request.method == 'PUT':
        wordlist = WordList.objects.get(id=id)
        serializer = WordListSerializer(instance=wordlist,data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response (serializer.data)

    if request.method == 'DELETE':
        wordlist = WordList.objects.get(id=id)
        wordlist.delete()
        return Response({'detail': 'Wordlist deleted successfully'})

# TODO Add the add word to DB logic
@api_view(['PUT'])
def wordlist_add_words(request,id):
    wordlist = WordList.objects.get(id=id)
    serializer = WordSerializer(instance=wordlist,data=request.data)
    for word in request.data['words']:
        if Word.objects.filter(word=word).count() == 0:
            pass
            # Add the word to the DB
        wordlist.words.add(Word.objects.get(word=word))
        wordlist.save()
    if serializer.is_valid():
        serializer.save()
    return Response ({'detail': 'Words were added to the word list successfully'})
#endregion
