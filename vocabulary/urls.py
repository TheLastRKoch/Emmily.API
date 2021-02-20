from django.urls import path
from vocabulary.views import *
from vocabulary.api_views import *

app_name = 'vocabulary'

urlpatterns = [
    # Words manage
	path('word', WordGetList.as_view() , name="list"),
	path('word/new', WordCreation.as_view(), name="create"),
	path('word/<int:id>', WordRetriveUpdateDestroy.as_view(), name="manage"),

	# WordList manage
	path('wordlist', WordListGetList.as_view() , name="list"),
	path('wordlist/new', WordListCreation.as_view(), name="create"),
	path('wordlist/<int:id>', WordListRetriveUpdateDestroy.as_view(), name="manage")
]