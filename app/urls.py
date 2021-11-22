from django.urls import include, path
from .views import *

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('question/create', PostQuestion.as_view()),
    path('question/get', GetQuestion.as_view()),
    path('all-questions/get', GetAllQuestion.as_view()),
    path('answer/create', PostAnswer.as_view()),
    path('answer/get', GetAnswer.as_view()),
    path('list-question/create', PostListQuestion.as_view()),
    path('list-question/get', GetListQuestion.as_view()),
    path('all-lists-question/get', GetAllListQuestion.as_view()),
    path('time-lists-question/update', UpdateTimeListQuestion.as_view()),
]
