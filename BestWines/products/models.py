from django.db import models

class Product(models.Model):
    product_code = models.CharField(max_length=100)  # Remove "unique=True" if present
    product_description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    size = models.CharField(max_length=50, blank=True, null=True)
    abv = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    brand = models.CharField(max_length=100, blank=True, null=True)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.product_code
