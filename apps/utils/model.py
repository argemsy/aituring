# Third-party Libraries
from django.db import models


class Auditable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    is_active = models.BooleanField(default=True, db_index=True)
    is_deleted = models.BooleanField(default=False, db_index=True)

    class Meta:
        abstract = True
