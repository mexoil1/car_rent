from django.db import models


class OrderingManager(models.Manager):
    '''Manager to orded queryset by title'''

    def get_queryset(self):
        return super().get_queryset().order_by('title')
