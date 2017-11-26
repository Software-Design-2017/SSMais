from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(max_length=500)
    price = models.FloatField(blank=False, null=False)

    def __str__(self):
        return self.name


class Combo(Service):
    specification = models.CharField(max_length=120)
    services = models.ManyToManyField(Service, through='ServiceCombo', related_name='services')

    def add(self, service):
        ServicesCombo.objects.create(service_combo=self, service_in_combo=service)

    def remove(self, service):
        service_combo = ServicesCombo.objects.filter(service_combo=self, service_in_combo=service)
        service_combo.delete()


class ServiceCombo(models.Model):
    service_combo = models.ForeignKey(Combo, related_name='service_combo')
    service_in_combo = models.ForeignKey(Service, related_name='service_in_combo')
