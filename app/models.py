from django.utils.timezone import localtime, localdate

from django.db import models


def get_current_time():
    return localtime().time().strftime('%H:%M:%S')


class ListQuestion(models.Model):
    name = models.CharField(max_length=100, unique=True)
    life_time = models.TimeField(default=get_current_time, blank=True)

    def __str__(self):
        return self.name


class Question(models.Model):
    question = models.CharField(max_length=250)
    list_question = models.ForeignKey(ListQuestion, on_delete=models.CASCADE, related_name='list')
    complete = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return f'Question №{self.pk} for List {self.list_question}'


class Answer(models.Model):
    YES = 'Yes'
    NO = 'No'
    answer = [
        (YES, 'Yes'),
        (NO, 'No')
    ]
    answer_choice = models.CharField('answer', choices=answer, max_length=3, null=True, blank=True)
    open_answer = models.CharField(max_length=100, blank=True, null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_get')

    def __str__(self):
        return f'Answer №{self.id} for {self.question}'
