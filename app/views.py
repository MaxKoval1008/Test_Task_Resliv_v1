from drf_spectacular.utils import extend_schema

from .permisions import IsAdmin
from .serializers import QuestionSerializer, ListQuestionSerializer, AnswerSerializer, UpdateTimeListQuestionSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView
from .models import Question, Answer, ListQuestion


@extend_schema(description='Create Question')
class PostQuestion(CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated & IsAdmin]


class GetQuestion(RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated & IsAdmin]


class GetAllQuestion(ListAPIView):
    queryset = ListQuestion.objects.all()
    serializer_class = ListQuestionSerializer
    permission_classes = [IsAuthenticated & IsAdmin]


@extend_schema(description='Create Answer')
class PostAnswer(CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated & IsAdmin]


class GetAnswer(RetrieveAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated & IsAdmin]


@extend_schema(description='Create Question list')
class PostListQuestion(CreateAPIView):
    queryset = ListQuestion.objects.all()
    serializer_class = ListQuestionSerializer
    permission_classes = [IsAuthenticated & IsAdmin]


class GetListQuestion(RetrieveAPIView):
    queryset = ListQuestion.objects.all()
    serializer_class = ListQuestionSerializer
    permission_classes = [IsAuthenticated & IsAdmin]


class GetAllListQuestion(ListAPIView):
    queryset = ListQuestion.objects.all()
    serializer_class = ListQuestionSerializer
    permission_classes = [IsAuthenticated & IsAdmin]


class UpdateTimeListQuestion(UpdateAPIView):
    queryset = ListQuestion.objects.all()
    serializer_class = UpdateTimeListQuestionSerializer
    permission_classes = [IsAuthenticated & IsAdmin]
