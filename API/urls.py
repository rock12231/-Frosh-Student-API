from django.urls import path
from API.views import UserList
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('get', UserList.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)