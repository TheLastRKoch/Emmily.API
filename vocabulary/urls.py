from django.urls import path
from rest_framework import views
from . import views

app_name = 'vocabulary'

urlpatterns = [
    # Words manage
	path('word',views.getWords , name="list"),
	path('word/<int:id>',views.WordRetriveUpdateDestroy , name="detail"),
	path('word/new', views.addNewWord, name="create"),

	# WordList manage
	#path('wordlist', WordListGetList.as_view() , name="list"),
	#path('wordlist/new', WordListCreation.as_view(), name="create"),
	#path('wordlist/<int:id>', WordListRetriveUpdateDestroy.as_view(), name="manage")
]