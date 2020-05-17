from django.db import models
from django.conf import settings
from utils.models.base_model import BaseModel
from django.utils.translation import ugettext_lazy as _


class TestResult(BaseModel):
    test = models.ForeignKey('tests.Test', on_delete=models.CASCADE, related_name='test_results')
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='test_results',
                             verbose_name=_('User'))
    is_finished = models.BooleanField(default=False, blank=True)
