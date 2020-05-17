from django.db import models
from utils.models.base_model import BaseModel
from django.utils.translation import ugettext_lazy as _


class Answer(BaseModel):
    question = models.ForeignKey('tests.Question', on_delete=models.CASCADE, related_name='answers')
    name = models.CharField(verbose_name=_('Answer name'), max_length=250)
    description = models.TextField(null=True, blank=True)
    is_correct = models.BooleanField(default=False, blank=True)
