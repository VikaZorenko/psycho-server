from django.contrib import admin
from .models import Answer, Question, QuestionResult, Test, TestResult, TestStat, TestStatResult

admin.site.register(Answer)
admin.site.register(Question)
admin.site.register(QuestionResult)
admin.site.register(Test)
admin.site.register(TestResult)
admin.site.register(TestStat)
admin.site.register(TestStatResult)
