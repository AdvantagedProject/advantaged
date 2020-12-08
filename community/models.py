from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Community (models.Model):
    leader = models.CharField(max_length=30)
    member = models.ManyToManyField("funding.Person")
    group_name = models.CharField(max_length=30)
    content = RichTextUploadingField()
    lat = models.DecimalField(max_digits=10, decimal_places=6, default=0)
    lng = models.DecimalField(max_digits=10, decimal_places=6, default=0)
    requirement = models.IntegerField(default=0)
    img = models.ImageField(blank = True)

class Post (models.Model) :
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    writer = models.ForeignKey("funding.Person", on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    content = RichTextUploadingField()
    img = models.ImageField(blank = True)
    timestamp = models.DateTimeField(auto_now_add=True)

class reply (models.Model) :
    post = models.ForeignKey(Post, models.CASCADE)
    writer = models.ForeignKey("funding.Person", on_delete=models.CASCADE)
    detail = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
