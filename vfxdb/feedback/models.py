from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class FeedBackPost(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    body= models.CharField(max_length=500)
    publisheddate= models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-publisheddate',)


    def __str__(self):
        return self.body[:200]