# Django.
import logging
from django import forms

from ..models import (Provider)


class OperatingHoursForm(forms.ModelForm):
    days_of_week = {'sunday', 'Sunday',
                    'monday', 'Monday',
                    'tuesday', 'Tuesday',
                    'wednesday', 'Wednesday',
                    'thirsday', 'Thirsday',
                    'friday', 'Friday',
                    'saturday', 'Saturday'}
    # Form Fields.
    day = forms.CharField(choice=days_of_week)
    open_hour = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))
    close_hour = forms.TimeField(widget=forms.TimeInput(format='%H:%M'))

    class Meta:
        model = Provider
        exclude = ['provider']
