from django.db import models
from utils.models.base_model import BaseModel
from django.utils.translation import ugettext_lazy as _


class TestStat(BaseModel):
    test = models.ForeignKey('tests.Test', on_delete=models.CASCADE, related_name='test_stats')
    name = models.CharField(verbose_name=_('Test stat name'), max_length=250)
    description = models.TextField(null=True, blank=True)
