from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from Emmily.services import DictionaryEn

from wordlist_skill.serializers import WordSerializer
from wordlist_skill.models import Word

class WordPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100

class WordList(ListAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filter_fields = ('id',)
    search_fields = ('word',"definition")
    pagination_class = WordPagination

    def get_queryset(self):
            #Filter by language
            request_language = self.request.query_params.get('ljs', None)
            queryset = Word.objects.all()
            if request_language is not None: 
                queryset = queryset.filter(
                    language=request_language
                )
            return queryset


class WordCreation(CreateAPIView):
    serializer_class = WordSerializer
    
    def create(self,request,*args,**kwargs):
        #Check if the word already exist
        if Word.objects.filter(word = request.data.get("word")).count() != 0:
            raise ValidationError({'word':'Already existe on the DB'})
        return super().create(request,*args,**kwargs)
    

class WordDestroy(DestroyAPIView):
    queryset = Word.objects.all()
    lookup_field = 'id'

    def delete(self,request,*args, **kwargs):
        #Clear cache
        product_id = request.data.get('id')
        response = super().delete(self,request,*args, **kwargs)
        if response.status_code == 204:
            from django.core.cache import cache
            cache.delete('product_data_{}'.format(product_id))
        return response
