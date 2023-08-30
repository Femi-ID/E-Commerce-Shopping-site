from django import forms
from django.utils.translation import gettext_lazy as _


class CouponApplyForm(forms.Form):
    code = forms.CharField(label=_('Coupon'))
# You have added a label to the code field and marked it for translation '_'.

# form to use for the user to enter a coupon code.
