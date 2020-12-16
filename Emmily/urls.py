from django.contrib import admin
from django.urls import path

import wordlist_skill.api_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/wordlist/',wordlist_skill.api_views.WordList.as_view())
]
