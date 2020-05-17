from django.db import models
from utils.models.base_model import BaseModel


class QuestionResult(BaseModel):
    question = models.ForeignKey('tests.Question', on_delete=models.CASCADE, related_name='question_results')
    answer = models.ForeignKey('tests.Answer', on_delete=models.CASCADE, related_name='question_results')
    test_result = models.ForeignKey('tests.TestResult', on_delete=models.CASCADE, related_name='question_results')
