from django.urls import path
from vocabulary.views import test
from vocabulary.api_views import *
from django.views.decorators.csrf import csrf_exempt

app_name = 'vocabulary'

urlpatterns = [
    # Words manage
	path('', WordGetList.as_view() , name="list"),
	path('new', WordCreation.as_view(), name="create"),
	path('<int:id>', WordRetriveUpdateDestroy.as_view(), name="manage"),

	# WordList manage
]