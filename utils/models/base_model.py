import uuid

from django.db import models
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):
    """
    Setups default class representation and adds created_date and
    modified_date database fields.
    """
    id = models.UUIDField(_("id"), primary_key=True, default=uuid.uuid4, editable=False)
    created_date = models.DateTimeField(_("created date"), auto_now_add=True)
    modified_date = models.DateTimeField(_("modified date"), auto_now=True)

    class Meta:
        abstract = True

    @property
    def is_new(self):
        return not self.created_date
