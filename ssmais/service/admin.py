from django.contrib import admin

# Local Django
from .models import (
    Service, Combo, ServiceCombo
)

admin.site.register(Service)
admin.site.register(Combo)
admin.site.register(ServiceCombo)
