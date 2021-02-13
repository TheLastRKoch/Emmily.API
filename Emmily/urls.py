from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from account.views import (
    registration_view,
    logout_view,
    login_view,
    account_view,
    must_authenticate_view,
    ObtainAuthTokenView
)

urlpatterns = [
    # REST-framwork
    path('api/v1/vocabulary/', include('vocabulary.urls')),
    
    path('admin/', admin.site.urls),
    path('account/', account_view, name="account"),
    path('api/v1/account/login', ObtainAuthTokenView.as_view(), name="login"),
    
    #url('',wordlist_skill.views.index)
]
