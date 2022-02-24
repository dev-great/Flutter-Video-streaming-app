from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    profilepix= models.ImageField(upload_to="profile/")


    def __str__(self) :
        return self.user.username


class OTPVerification(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    phonenumber= models.IntegerField(blank=False)
    isVerified = models.BooleanField(blank=False, default=False)
    counter = models.IntegerField(default=0, blank=False)
    
    def __str__(self):
        return self.user.email

class Subscriber(models.Model):
    CATEGORY_OPTIONS = [
        ('WEEKLY', 'WEEKLY'),
        ('MONTHLY', 'MONTHLY'),
        ('BIMONTHLY', 'BIMONTHLY'),
        ('YEARLY', 'YEARLY')
    ]

    category = models.CharField(choices=CATEGORY_OPTIONS, max_length=11)
    amount = models.DecimalField(max_digits=10, decimal_places=2, max_length=10)
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    startdate = models.DateField()
    enddate = models.DateField()

    class Meta:
        ordering = ('-enddate',)

    def __str__(self):
        return  f"User={self.user.username}|Sucscription={self.category}"

