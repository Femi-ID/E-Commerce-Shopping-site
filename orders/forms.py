from django import forms
from .models import Order

"""Form to enter the order details. This form will be used to create new Order objects"""


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']

# Form created based on the Order model

