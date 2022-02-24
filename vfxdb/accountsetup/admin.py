from django.contrib import admin
from .models import Profile, OTPVerification, Subscriber

admin.site.register([Profile, OTPVerification, Subscriber])
# Register your models here.
