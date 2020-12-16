from rest_framework.generics import ListAPIView

from wordlist_skill.serializers import WordSerializer
from wordlist_skill.models import Word

class WordList(ListAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
