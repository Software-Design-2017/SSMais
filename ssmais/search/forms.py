# Django.
import logging
from django import forms

class SearchForm(forms.Form):
    # Form Fields.
    name = forms.CharField(label='Nome', required=True)
