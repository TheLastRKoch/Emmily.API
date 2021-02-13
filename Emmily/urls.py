from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from account.views import (
    registration_view,
    logout_view,
    login_view,
    account_view,
    must_authenticate_view,
    ObtainAuthTokenView
)

import  wordlist_skill.api_views
import  wordlist_skill.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', account_view, name="account"),
    path('api/v1/account/login', ObtainAuthTokenView.as_view(), name="login"),

    path('api/v1/wordlist/', wordlist_skill.api_views.WordGetList.as_view()),
    path('api/v1/wordlist/new', wordlist_skill.api_views.WordCreation.as_view()),
    path('api/v1/wordlist/<int:id>', wordlist_skill.api_views.WordRetriveUpdateDestroy.as_view()),

    url('',wordlist_skill.views.index)
]
