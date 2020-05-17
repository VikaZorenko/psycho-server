from django.db import models
from utils.models.base_model import BaseModel
from django.utils.translation import ugettext_lazy as _


class Question(BaseModel):
    test = models.ForeignKey('tests.Test', on_delete=models.CASCADE, related_name='questions')
    test_stat = models.ForeignKey('tests.TestStat', on_delete=models.CASCADE, related_name='questions')
    name = models.CharField(verbose_name=_('Question name'), max_length=250)
    description = models.TextField(null=True, blank=True)
    points = models.IntegerField(default=1, blank=True)
