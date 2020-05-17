from django.db import models
from utils.models.base_model import BaseModel
from django.utils.translation import ugettext_lazy as _


class Test(BaseModel):
    name = models.CharField(verbose_name=_('Test name'), max_length=250)
    description = models.TextField(null=True, blank=True)
