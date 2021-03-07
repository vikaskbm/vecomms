from django import forms
from django_countries.fields import CountryField


class CheckoutForm(forms.Form):
    address_line_1 = forms.CharField()
    address_line_2 = forms.CharField(required=False)

    country = CountryField(blank_label='(select country)')
    zip_code = forms.CharField()

    same_billing_address = forms.BooleanField(widget=forms.CheckBoxInput())
    save_info = forms.BooleanField(widget=forms.CheckBoxInput())

    payment_option = forms.BooleanField(widget=forms.RadioSelect())
    
