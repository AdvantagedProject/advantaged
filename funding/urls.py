from django.urls import path, re_path
from funding import views

app_name = 'funding'

urlpatterns = [
    path('create/', views.funding_create, name="funding_create"),
    path('detail/<int:pk>/', views.funding_detail, name="funding_detail"),
]