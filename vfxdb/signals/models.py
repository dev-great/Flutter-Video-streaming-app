from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Signals(models.Model):
    title=models.CharField(max_length=50, blank=True, null=True)
    Buy= models.IntegerField(blank=True, null=True)
    TP= models.IntegerField(blank=True, null=True)
    SL= models.IntegerField(blank=True, null=True)
    body= models.TextField(max_length=200,blank=True, null=True)
    video = models.FileField(upload_to='documents/', blank=True, null=True)
    PostImage= models.ImageField(upload_to="signals/feedpost/",blank=True, null=True)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    publisheddate= models.DateTimeField(auto_now_add=True)
    updateddate= models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-publisheddate',)

    def __str__(self):
        return self.title