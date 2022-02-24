from django.db import models

# Create your models here.

class NotificationPost(models.Model):
    title = models.CharField(max_length=100)
    body= models.CharField(max_length=500)
    publisheddate= models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-publisheddate',)


    def __str__(self):
        return self.body[:100]