from django import forms
from localflavor.us.forms import USZipCodeField
from .models import Order

"""Form to enter the order details. This form will be used to create new Order objects"""


class OrderCreateForm(forms.ModelForm):
    postal_code = USZipCodeField()

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']

# Form created based on the Order model
# read the django-localflavor documentation and see all available local
# components for each country at https://django-localflavor.readthedocs.io/en/latest/.
