from django.urls import path  
from . import views

urlpatterns=[
    path('', views.FeedBackView.as_view(), name="feedback"),
]