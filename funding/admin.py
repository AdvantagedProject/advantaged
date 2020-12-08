from django.contrib import admin
from funding import models
# Register your models here.

admin.site.register(models.Person)
admin.site.register(models.Funding)
admin.site.register(models.Order)

