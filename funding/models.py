from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Person(models.Model):
    base_data = models.OneToOneField(User, on_delete=models.CASCADE)
    current_point = models.IntegerField(default=0)
    age = models.IntegerField(default=0)
    phone_number = models.CharField(max_length=14)
    category = models.IntegerField(default=0)
    photo = models.ImageField(blank=True)
    location = models.CharField(max_length=20 , blank=True)
    certificate = models.ImageField(blank=True)

class Funding(models.Model) :
    community = models.ForeignKey("community.Community", on_delete=models.CASCADE)
    writer = models.ForeignKey(Person, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = RichTextUploadingField()
    img = models.ImageField(blank = True)
    target_amout = models.IntegerField(default=0)
    funded_amout = models.IntegerField(default=0)
    is_finished = models.BooleanField(default = False)

    option_num = models.IntegerField(default=1)
    option_1_name = models.CharField(max_length=30, blank = True)
    option_1_price = models.IntegerField(default=0)
    option_2_name = models.CharField(max_length=30,blank = True)
    option_2_price = models.IntegerField(default=0)
    option_3_name = models.CharField(max_length=30,blank = True)
    option_3_price = models.IntegerField(default=0)


class Order(models.Model) : 
    Funding = models.ForeignKey(Funding, on_delete=models.CASCADE)
    customer = models.ForeignKey(Person, on_delete=models.CASCADE)
    option_num = models.IntegerField(default = 1)
    is_paid = models.BooleanField(default = False)
    is_delivered = models.BooleanField(default = False)

