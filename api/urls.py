from django.urls import include, path
from mlapi import views

urlpatterns = [
    path("predict", views.digit_predict)
]
