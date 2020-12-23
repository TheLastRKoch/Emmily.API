from django.contrib import admin
from django.urls import path

import  wordlist_skill.api_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/wordlist/', wordlist_skill.api_views.WordList.as_view()),
    path('api/v1/wordlist/new', wordlist_skill.api_views.WordCreation.as_view()),
    path('api/v1/wordlist/delete/<int:id>', wordlist_skill.api_views.WordDestroy.as_view())
]
