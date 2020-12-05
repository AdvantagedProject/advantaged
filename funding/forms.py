from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Funding

class FundAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())
    class Meta:
        model = Funding
        fields = '__all__'

class FundAdmin(admin.ModelAdmin):
    form = FundAdminForm

admin.site.register(Funding, FundAdmin)