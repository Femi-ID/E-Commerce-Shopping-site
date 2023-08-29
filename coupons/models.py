from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    active = models.BooleanField()

    def __str__(self):
        return self.code


"""
coupons will be valid for customers in a certain time frame. 
The coupons will not have any limitations in terms of the number of times they can be redeemed, 
and they will be applied to the total value of the shopping cart.
"""
