from django.db import models


class BaseAbstractModel(models.Model):
    created_at = models.DateTimeField(
        editable=False, auto_now_add=True, db_index=True,
        verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        editable=False, auto_now=True, db_index=True,
        verbose_name="Дата изменения"
    )

    class Meta:
        abstract = True
