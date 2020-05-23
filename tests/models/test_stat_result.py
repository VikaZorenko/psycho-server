from django.db import models
from utils.models.base_model import BaseModel


class TestStatResult(BaseModel):
    test_result = models.ForeignKey('tests.TestResult', on_delete=models.CASCADE, related_name='test_stat_results')
    test_stat = models.ForeignKey('tests.TestStat', on_delete=models.CASCADE, related_name='test_stat_results')
    points = models.IntegerField(default=0, blank=True)
