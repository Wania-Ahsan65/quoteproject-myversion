from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=20, default='000')  # Re-added
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.name
    