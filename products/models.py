from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    price = models.FloatField(default=1.0)
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return '{}, price is= {:.2f}'.format(self.name, self.price)
