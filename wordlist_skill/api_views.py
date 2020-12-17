from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from wordlist_skill.serializers import WordSerializer
from wordlist_skill.models import Word

class WordList(ListAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filter_fields = ('id',)
    search_fields = ('word',"definition")

    def get_queryset(self):
            #Filter by language
            request_language = self.request.query_params.get('ljs', None)
            queryset = Word.objects.all()
            if request_language is not None: 
                queryset = queryset.filter(
                    language=request_language
                )
            return queryset
