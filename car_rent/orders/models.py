from django.db import models
from django.utils.translation import gettext_lazy as _

from core.models import BaseAbstractModel
from users.models import User
from cars.models import Car


class Order(BaseAbstractModel):
    """Model of order"""

    class OrderStatus(models.TextChoices):
        UNDER_CONSIDERATION = 'UC', _("На рассмотрении")
        ACCEPTED = 'AD', _("Одобрен")
        REJECTED = 'RD', _("Отклонен")

    сar = models.ForeignKey(
        Car, on_delete=models.CASCADE,
        verbose_name="Арендованный автомобиль"
    )
    renter = models.ForeignKey(
        User, on_delete=models.CASCADE,
        verbose_name="Арендатор"
    )
    #  связь с чатом по заказу

    desired_date = models.DateTimeField(
        verbose_name="До какого времени аренда"
    )
    start_rent_time = models.DateTimeField(
        verbose_name="Время начала аренды",
        null=True, blank=True
    )
    status = models.CharField(
        verbose_name="Статус",
        max_length=2,
        choices=OrderStatus.choices,
        default=OrderStatus.UNDER_CONSIDERATION,
    )

    class Meta:
        db_table = 'order_table'
    
