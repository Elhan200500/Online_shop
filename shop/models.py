from django.conf import settings
from django.db import models


class Product(models.Model):
    """Товар."""
    name = models.CharField(verbose_name='Title', max_length=128)
    description = models.TextField(default='')
    price = models.DecimalField(decimal_places=2, max_digits=10)
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name
