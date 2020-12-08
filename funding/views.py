from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User

from django.http import HttpResponse
from Advantaged import settings
from funding import forms as funding_forms
from funding import models as funding_models
# Create your views here.

def test(request):
    return None

def logout(request):
    auth_logout(request)
    return None


def signup(request):
    if request.method == "POST":
        form = funding_forms.UserForm(request.POST)
        form2 = funding_forms.PersonForm_1(request.POST)
        if form.is_valid() and form2.is_valid() :
            new_user = User.objects.create_user(**form.cleaned_data)
            person_data = form2.cleaned_data
            new_person = funding_models.Person.objects.create(base_data=new_user, age=person_data.get("age"), phone_number=person_data.get("phone_number"), photo=person_data.get("photo"))
            auth_login(request, new_user)
            return render(request, 'funding/signup.html')            # return redirect('funding:main')
    else:
        form = funding_forms.UserForm() 
        form2 = funding_forms.PersonForm_1()
        return render(request, 'funding/signup.html', {'form': form, 'form2':form2})


def funding_create(request):
    if request.method == "POST":
        form = funding_forms.FundAdminForm(request.POST)
        if form.is_valid() :
            form.save()
            return HttpResponse("저장됨")
        else:
            return HttpResponse("저장 실패")
    else:
        form = funding_forms.FundAdminForm()
        return render(request, "funding/create_funding.html", {'form': form})

def funding_detail(request, pk):
    funding = get_object_or_404(funding_models.Funding, pk=pk)
    return render(request, "funding/funding_detail.html", {'funding': funding})
