# Django.
from django import forms
from django.utils.translation import ugettext_lazy as _

# Local Django.
from ..models import User


class RegisterForm(forms.ModelForm):
    # Form Fields.
    name = forms.CharField(label='NAME',
                           max_length=60)

    email = forms.EmailField(label='EMAIL')

    class Meta:
        model = User
        fields = [
            'name',
            'email'
        ]

    # Front-end validation function for client register page.
    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        password_confirmation = self.cleaned_data.get('password_confirmation')

        email_from_database = User.objects.filter(email=email)

        if email_from_database.exists():
            raise forms.ValidationError(('Email already registered'))
        elif len(password) < 8:
            raise forms.ValidationError(
                ('Password must be between 8 and 12 characters'))
        elif len(password) > 12:
            raise forms.ValidationError(
                ('Password must be between 8 and 12 characters'))
        elif password != password_confirmation:
            raise forms.ValidationError(('Passwords do not match.'))

        return super(RegisterForm, self).clean(*args, **kwargs)


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(
        widget=forms.PasswordInput, label=_('Password'))

    def clean(self, *args, **kwargs):
        password = self.cleaned_data.get("password")

        if len(password) < 8:
            raise forms.ValidationError(
                {'password': [_('Password must be between 8 and 12 characters')]})
        elif len(password) > 12:
            raise forms.ValidationError(
                {'password': [_('Password must be between 8 and 12 characters')]})
        else:
            pass

        return super(LoginForm, self).clean(*args, **kwargs)

    class Meta:
        model = User
