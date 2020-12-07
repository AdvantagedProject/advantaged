from django.shortcuts import render, get_object_or_404
from funding import forms as funding_forms
from funding import models as funding_models
from django.http import HttpResponse
from Advantaged import settings


# Create your views here.

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