from django import forms
from django_countries.fields import CountryField

PAYMENT_CHOICES = (
    ('S', 'Stripe'),
    ('P', 'Paypal')
)



class CheckoutForm(forms.Form):
    address_line_1 = forms.CharField()
    address_line_2 = forms.CharField(required=False)

    country = CountryField(blank_label='(select country)')
    zip_code = forms.CharField()

    same_billing_address = forms.BooleanField(widget=forms.CheckboxInput ())
    save_info = forms.BooleanField(widget=forms.CheckboxInput())

    payment_option = forms.ChoiceField(widget=forms.RadioSelect, choices=PAYMENT_CHOICES)

