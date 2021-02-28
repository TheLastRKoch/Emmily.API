from django.urls import path
from rest_framework import views
from . import views

app_name = 'vocabulary'

urlpatterns = [
    # Words manage
	path('word',views.word_list_add , name="get_words"),
	path('word/<int:id>',views.word_retrive_update_destroy , name="word_retrive_update_destroy"),

	# WordList manage
	path('wordlist', views.wordlist_list_add , name="get_wordlists"),
	path('wordlist/<int:id>', views.wordlist_retrive_update_destroy, name="wordlist_retrive_update_destroy"),
	path('wordlist/<int:id>/manage-words', views.wordlist_manage_words, name="wordlist-add-word")
]