from django.contrib import admin
from django.urls import path
from tokens.views import tokens as token_v

urlpatterns = [
    path('token/', token_v.TokenCreateAPIView.as_view(), name='create-token'),
]
