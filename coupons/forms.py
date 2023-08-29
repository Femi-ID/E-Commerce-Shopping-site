from django import forms


class CouponApplyForm(forms.Form):
    code = forms.CharField()


# form to use for the user to enter a coupon code.
