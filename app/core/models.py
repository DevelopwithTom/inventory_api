from django.db import models
import uuid


class Product(models.Model):
    """ Creates and saves a new product """
    sku = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    quantity = models.IntegerField(blank=False, null=False)
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return "Name: %s, Quantity Available: '%s', Price: £%s" %(self.name, self.quantity, self.price)
