from django.db import models
from django.core.exceptions import ValidationError

def validate_length(value, length=10):
    if len(value) != length:
        raise ValidationError(f"phone number should be of length {length}")

# Create your models here.
class Customer(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_phno = models.CharField(max_length=10, validators=[validate_length])
    customer_addr = models.TextField(max_length=255)
    insert_dt = models.DateTimeField()
    update_dt = models.DateTimeField()

    def __str__(self):
        return self.customer_name


class Orders(models.Model):
    ORDER_STATUS = [
        ('C', 'Completed'),
        ('N', 'Not Done'),
        ('D', 'Delivered'),
    ]
    order_id = models.CharField(max_length=50, unique=True)
    item_id = models.CharField(max_length=50)
    item_name = models.CharField(max_length=100)
    qty = models.IntegerField()
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_dt = models.DateTimeField()
    update_dt = models.DateTimeField()
    order_status = models.CharField(max_length=1, choices=ORDER_STATUS, default='N')


    def __str__(self):
        return self.item_name


class Payments(models.Model):
    order_id = models.ForeignKey(Orders, to_field='order_id', on_delete=models.CASCADE)
    paid_amount = models.FloatField()
    payment_dt = models.DateTimeField()
    updated_dt = models.DateTimeField()

    def __str__(self):
        return self.payment_dt.strftime("%m/%d/%Y, %H:%M:%S")
