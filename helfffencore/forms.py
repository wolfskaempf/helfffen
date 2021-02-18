from django import forms

from .models import HelpOffer

class HelpOfferForm(forms.ModelForm):
    class Meta:
        model = HelpOffer
        fields = ['name', 'contact', 'additional_information']
        exclude = ("task",)
