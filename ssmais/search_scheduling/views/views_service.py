from django.core.urlresolvers import reverse_lazy
from django.db import transaction
from django.views.generic import CreateView, ListView, FormView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect

from ..models import (
    Service, Combo
)

from ..forms import (
    ComboForm
)


class ServiceComboCreate(CreateView):
    model = Combo
    fields = ['name', 'specification', 'description', 'price']
    template_name = None
    success_url = None
    provider = None


    def get_context_data(self, **kwargs):
        self.set_provider()
        data = super(ServiceComboCreate, self).get_context_data(**kwargs)
        combo_form = ComboForm(provider=self.provider)

        if self.request.POST:
            data['services'] = combo_form.ServiceComboFormSet(self.request.POST)
        else:
            data['services'] = combo_form.ServiceComboFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        services = context['services']

        with transaction.atomic():
            if services.is_valid():
                services_validate = self._validate_quantity(services, form)
            else:
                return super(ServiceComboCreate, self).form_invalid(form)

            # Register combo and your creator
            self.object = form.save(commit=False)
            self.object.provider = self.provider
            self.object.save()

            for service_in_combo in services_validate:
                    self.object.combo.add(service_in_combo)

            self.object.combo.save()
        return super(ServiceComboCreate, self).form_valid(form)

    def _validate_quantity(self, services, form):
        if len(services) > 1:
            services_validate = []
            number_of_filled = len(services)

            # Checks the number of forms filled
            for service_compound in services:
                get_service = service_compound.cleaned_data.get('service_in_combo')

                # Case form is filled the object is add in list of combo
                if get_service:
                    services_validate.append(service_compound.cleaned_data.get('service_in_combo'))
                else:
                    number_of_filled = number_of_filled - 1

            if number_of_filled > 1:
                return services_validate
            else:
                return super(ServiceComboCreate, self).form_invalid(form)
        else:
            return super(ServiceComboCreate, self).form_invalid(form)

    def set_provider(self):
        self.provider = None
