from django import forms

from ssmais.service.models import (
    Service, Combo, ServiceCombo
)


class ServiceForm(forms.ModelForm):
    provider_create = None

    def __init__(self, **kw):
        super(ServiceForm, self).__init__(**kw)
        self.fields['service_in_combo'].queryset = Service.objects.filter(provider=self.provider_create,
                                                                          combo__isnull=True)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    @staticmethod
    def __create_service_form__(provider):
        ServiceForm.provider_create = provider
        return ServiceForm

    class Meta:
        model = ServiceCombo
        fields = ['service_in_combo']


class ComboForm():
    provider = None
    ServiceComboFormSet = forms.inlineformset_factory(Combo, ServiceCombo,
                                                      form=ServiceForm, extra=0,
                                                      fk_name='service_combo',
                                                      min_num=2, validate_min=True)

    def __init__(self, provider):
        self.ServiceComboFormSet.form = ServiceForm.__create_service_form__(provider=provider)


class BaseServiceForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(FormService, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Service
        exclude = ['provider']
