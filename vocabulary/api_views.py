from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.exceptions import ValidationError
from vocabulary.serializers import WordListSerializer, WordSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.filters import SearchFilter
from vocabulary.models import Word, WordList

class Pagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100

#region Word

class WordGetList(ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filter_fields = ('id',)
    search_fields = ('word',"definition")
    pagination_class = Pagination

    def get_queryset(self):
            #Filter by language
            request_language = self.request.query_params.get('lan', None)
            queryset = Word.objects.all()
            if request_language is not None: 
                queryset = queryset.filter(
                    language=request_language
                )
            return queryset

class WordCreation(CreateAPIView):
    permission_classes = [IsAdminUser]
    serializer_class = WordSerializer
    
    def create(self,request,*args,**kwargs):
        #Check if the word already exist
        if Word.objects.filter(word = request.data.get("word")).count() != 0:
            raise ValidationError({'word':'Already existe on the DB'})
        return super().create(request,*args,**kwargs)   

class WordRetriveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Word.objects.all()
    lookup_field = 'id'
    serializer_class = WordSerializer

    def delete(self,request,*args, **kwargs):
        #Clear cache
        product_id = request.data.get('id')
        response = super().delete(self,request,*args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('product_data_{}'.format(product_id))
        return response

    def update(self,request,*args, **kwargs):
        response = super().update(request,*args, **kwargs)
        if response.status_code == 200:
            from django.core.cache import cache
            word = response.data
            cache.set('word_data_{}'.format(word['id']),{
                'word': word['word'],
                'language': word['language'],
                'phonetic': word['phonetic'],
                'definition': word['definition'],
                'urban_definition': word['urban_definition'],
                'example': word['example']
            })
        return response

#endregion


