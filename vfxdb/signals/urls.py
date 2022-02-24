from django.urls import path  
from . import views

urlpatterns=[
    path('', views.SignalView.as_view(), name="signals"),
]