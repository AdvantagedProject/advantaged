from django import forms
from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib.auth.models import User
from ckeditor.widgets import CKEditorWidget

from .models import Funding, Person

class FundAdminForm(forms.ModelForm):
    class Meta:
        model = Funding
        fields = '__all__'

class FundAdmin(admin.ModelAdmin):
    form = FundAdminForm

class PersonForm_1(forms.ModelForm):
    class Meta:
        model =  Person
        fields = ['age', 'phone_number', 'photo']


class PersonForm_2(forms.ModelForm):
    class Meta:
        model =  Person
        fields = ['age', 'phone_number', 'photo', 'location', 'certificate']

class UserForm(forms.ModelForm):
    class Meta:
        model =  User
        fields = ['username', 'password', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'id':'id'})
        self.fields['password'].widget.attrs.update({'id':'pw'})
        self.fields['last_name'].widget.attrs.update({'id':'name'})
        self.fields['email'].widget.attrs.update({'id':'email'})

