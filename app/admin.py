from django.contrib import admin
from .models import ListQuestion, Question, Answer

admin.site.register(Question)
admin.site.register(ListQuestion)
admin.site.register(Answer)
