from django.contrib import admin

from .models import User

from .models import (
Service, Combo, ServiceCombo
)

from .models import (
Provider
)

class UserAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_active']


admin.site.register(User, UserAdmin)


admin.site.register(Service)
admin.site.register(Combo)
admin.site.register(ServiceCombo)


admin.site.register(Provider)
