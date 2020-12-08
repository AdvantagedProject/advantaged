from django.contrib import admin
from community import models
# Register your models here.

admin.site.register(models.Community)
admin.site.register(models.Post)
admin.site.register(models.reply)