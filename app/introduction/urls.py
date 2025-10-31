from django.urls import path
from app.introduction.views import introView

urlpatterns = [
    path("", introView, name="intro"),
]
