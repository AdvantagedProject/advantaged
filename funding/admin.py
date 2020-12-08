from django.contrib import admin
from funding.models import Person, Funding, Order

# Register your models here.

admin.site.register(Person)
admin.site.register(Funding)
admin.site.register(Order)