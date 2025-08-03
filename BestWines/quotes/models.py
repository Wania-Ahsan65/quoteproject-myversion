from django.conf import settings
from django.db import models
from products.models import Product

class Quote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"Quote #{self.id} - {self.customer_name}"

class QuoteItem(models.Model):
    quote = models.ForeignKey(Quote, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, blank=True)
    cost_price = models.DecimalField(max_digits=10, decimal_places=2)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    margin = models.DecimalField(max_digits=5, decimal_places=2, help_text="In %")
    discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def get_total(self):
        return self.selling_price * self.quantity
