from rest_framework import serializers
from .models import ListQuestion, Answer, Question


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class ListQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListQuestion
        fields = '__all__'


class UpdateTimeListQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListQuestion
        fields = ('life_time',)
        read_only_fields = ['name']
