from django import forms
from django.utils.translation import gettext_lazy as _

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    """
    A form for adding products to a shopping cart
    """
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,
                                      coerce=int, label=_('Quantity'))
    override = forms.BooleanField(required=False, initial=False,
                                  widget=forms.HiddenInput)
