from django.db import models

# Create your models here.

class FeedPost(models.Model):
    body= models.TextField(max_length=200)
    video = models.FileField(upload_to='documents/', blank=True, null=True)
    PostImage= models.ImageField(upload_to="feedpost/",  blank=True, null=True)
    addImage1=models.ImageField(upload_to="feedpost/", blank=True, null=True)
    addImage2=models.ImageField(upload_to="feedpost/", blank=True, null=True)
    addImage3=models.ImageField(upload_to="feedpost/", blank=True, null=True)
    publisheddate= models.DateTimeField(auto_now_add=True)
    updateddate= models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-publisheddate',)


    def __str__(self):
        return self.body[:100]