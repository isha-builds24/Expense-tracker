# from django.db import models

# # Create your models here.
# class Expense(models.Model):
#     name = models.CharField(max_length=200)
#     amount = models.IntegerField()
#     category = models.CharField(max_length=300)
#     date = models.DateField(auto_now=True) # (auto_now=True)date would be set to the current date in which the item wass added

#     def __str__(self):
#         return self.name      # each expense would be represented by its name



from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    class PaymentMethod(models.TextChoices):
        CASH = 'CASH', 'Cash'
        CREDIT_CARD = 'CREDIT_CARD', 'Credit Card'
        UPI = 'UPI', 'UPI'
        BANK_TRANSFER = 'BANK_TRANSFER', 'Bank Transfer'

    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True, related_name='expenses')
    name = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)
    payment_method = models.CharField(
        max_length=50, 
        choices=PaymentMethod.choices, 
        default=PaymentMethod.CASH
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.amount} ({self.category})"